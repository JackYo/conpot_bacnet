#### My operating system is Ubuntu 16.04.3 LTS on VMware, Conpot version 0.5.1

##### clone the repository from original conpot
`$ git clone https://github.com/mushorg/conpot.git`
 
##### step into the folder
`$ cd conpot`

##### check the revision tag
`$ git tag -l`


##### checkout the target revision tag, and your code will change to the version of Release_0.5.1
`$ git checkout tags/Release_0.5.1`


##### install conpot
`$ python setup.py install`


##### go to the path conpot installed and check if there are (only) folders named "conpot", "bin" and "EGG-INFO"
`$ ls /usr/local/lib/python2.7/dist-packages/Conpot-0.5.1-py2.7.egg/`



#### copy our conpot folder and replace the installed conpot folder, you can do something like this:
```bash
cd ~
sudo git clone https://github.com/JackYo/conpot_bacnet.git
sudo cp -r /usr/local/lib/python2.7/dist-packages/Conpot-0.5.1-py2.7.egg/conpot \
/usr/local/lib/python2.7/dist-packages/Conpot-0.5.1-py2.7.egg/conpot.bak
sudo cp -rf ~/conpot_bacnet/conpot/. /usr/local/lib/python2.7/dist-packages/Conpot-0.5.1-py2.7.egg/conpot/
```
#### Now, you should have accomplished all setup. Try the following command to run conpot.
`$ sudo conpot -f --template default`

#### BACnet service will listen on port 47808
If you see console output "Bacnet server started on: ('0.0.0.0', 47808)", everything should be right.

#### I recommend using [YABE](https://sourceforge.net/projects/yetanotherbacnetexplorer/) to test BACnet service.
You can refer to the screenshots in YabeUsage folder in this repository.
