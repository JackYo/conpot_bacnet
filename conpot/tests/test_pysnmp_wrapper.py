# Copyright (C) 2013  Johnny Vestergaard <jkv@unixcluster.dk>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import gevent.monkey
gevent.monkey.patch_all()

import unittest
import tempfile
import shutil
import os

from conpot.protocols.snmp.build_pysnmp_mib_wrapper import mib2pysnmp, find_mibs, compile_mib
from conpot.protocols.snmp import command_responder


class TestBase(unittest.TestCase):

    def setUp(self):
        self.mib_file = reduce(os.path.join, 'conpot/tests/data/VOGON-POEM-MIB.mib'.split('/'))

    def test_wrapper_processing(self):
        """
        Tests that the wrapper can process a valid mib file without errors.
        """
        tmpdir = tempfile.mkdtemp()
        result = mib2pysnmp(self.mib_file, tmpdir)
        self.assertTrue(result and self.check_content(os.path.join(tmpdir, 'VOGON-POEM-MIB.py')),
                        'mib2pysnmp2 did not generate the expected output.')

    def check_content(self, pyfile):
        ret = False
        with open(pyfile) as f:
            for l in f.readlines():
                if 'mibBuilder.exportSymbols("VOGON-POEM-MIB"' in l:
                    ret = True
                    break

        return ret

    def test_wrapper_output(self):
        """
        Tests that the wrapper generates output that can be consumed by the command responder.
        """
        tmpdir = None

        try:
            result = None
            tmpdir = tempfile.mkdtemp()

            if mib2pysnmp(self.mib_file, tmpdir):
                cmd_responder = command_responder.CommandResponder('', 0, [tmpdir])
                cmd_responder.snmpEngine.msgAndPduDsp.mibInstrumController.mibBuilder.loadModules('VOGON-POEM-MIB')
                result = cmd_responder._get_mibSymbol('VOGON-POEM-MIB', 'poemNumber')

            self.assertIsNotNone(result, 'The expected MIB (VOGON-POEM-MIB) could not be loaded.')
        finally:
            shutil.rmtree(tmpdir)

    def test_find(self):
        """
        Tests that the wrapper can find mib files.
        """
        input_dir = None
        try:
            input_dir = tempfile.mkdtemp()
            input_file = self.mib_file
            shutil.copy(input_file, input_dir)
            available_mibs = find_mibs([input_dir])
            self.assertIn('VOGON-POEM-MIB', available_mibs)
        finally:
            shutil.rmtree(input_dir)

    def test_compile(self):
        """
        Tests that the wrapper can output mib files.
        """
        input_dir = None
        output_dir = None
        try:
            input_dir = tempfile.mkdtemp()
            output_dir = tempfile.mkdtemp()
            shutil.copy(self.mib_file, input_dir)
            find_mibs([input_dir])
            compile_mib('VOGON-POEM-MIB', output_dir)
            self.assertIn('VOGON-POEM-MIB.py', os.listdir(output_dir))
        finally:
            shutil.rmtree(input_dir)
            shutil.rmtree(output_dir)
