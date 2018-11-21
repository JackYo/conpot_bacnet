#### My operation system is Ubuntu 16.04.3 LTS on VMware, Conpot version 0.5.1

##### clone the project from original conpot
`$ git clone https://github.com/mushorg/conpot.git`
 
##### step into the folder
`cd conpot`

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
