vcf
===

vcard file manipulator programs written in python 2.7

Usage
-----

*vdown* downgrade the version 4 vcard files to version 3.


Local try

```bash
PYTHONPATH=./lib:$PYTHONPATH ./bin/vdown < 
```


Install
-------

vcf depends on lxml and vobject third party python packages. 

```bash
sudo apt-get install python-lxml
sudo apt-get install python-vobject
sudo python setup.py install
```

Test
----

vcf is tested under Ubuntu 14.04 with python 2.7.6.

