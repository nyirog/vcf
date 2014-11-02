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
N:Blaha;Lujza;;Mrs.;
TEL;VALUE=uri:tel:5551234567
REV:20080424T195243Z
END:VCARD
BEGIN:VCARD
VERSION:4.0
FN:Gipsz Jakab
N:Gipsz;Jakab;;Dr.;
TEL;VALUE=uri:tel:5557654321
REV:20080424T195243Z
END:VCARD

$ PYTHONPATH=./lib:$PYTHONPATH ./bin/vdown < test/data/v4-backup.vcf
START:VCARD
VERSION:3.0
REV:2008-04-24T19:52:43Z
TEL;TYPE=None:5551234567
FN:Blaha Lujza
N:Blaha;Lujza;;Mrs.;
END:VCARD
START:VCARD
VERSION:3.0
REV:2008-04-24T19:52:43Z
TEL;TYPE=None:5557654321
FN:Gipsz Jakab
N:Gipsz;Jakab;;Dr.;
END:VCARD
```


Install
-------

```bash
sudo python setup.py install
```

Test
----

vcf is tested under Ubuntu 14.04 with python 2.7.6.

