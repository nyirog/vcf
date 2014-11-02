vcf
===

vcard file manipulator programs written in python 2.7

Usage
-----

*vdown* downgrade the version 4 vcard files to version 3.


For local try please setup PYTHONPATH

```bash
$ cat test/data/v4-backup.vcf
BEGIN:VCARD
VERSION:4.0
FN:Blaha Lujza
N:;Blaha Lujza;;;
TEL;VALUE=uri:tel:5551234567
REV:20080424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:4.0
FN:Gipsz Jakab
N:Gipsz Jakab;;;
TEL;VALUE=uri:tel:5557654321
REV:20080424T195243Z
END:VCARD

$ PYTHONPATH=./lib:$PYTHONPATH ./bin/vdown < test/data/v4-backup.vcf
BEGIN:VCARD
VERSION:3.0
FN:Blaha Lujza
N:;Blaha Lujza;;;
REV:2008-04-24T19:52:43Z
TEL:5551234567
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Gipsz Jakab
N:Gipsz Jakab;;;;
REV:2008-04-24T19:52:43Z
TEL:5557654321
END:VCARD
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

