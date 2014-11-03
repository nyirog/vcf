from re import compile, VERBOSE

def factory(line):
    for subclass in Component.__subclasses__():
        if subclass.match(line):
            return subclass
    raise InvalidTag(line)

class InvalidTag(Exception):
    pass

class Component(dict):
    single = True
    pattern = compile('')
    tag = ''

    def __init__(self, line):
        data = self.pattern.match(line).groupdict()
        dict.__init__(self, data)
        self._convert()
        return

    def _convert(self):
        return

    @classmethod
    def match(cls, line):
        return cls.pattern.match(line)

    def dump(self):
        return self.tag % self

class begin(Component):
    single = True
    pattern = compile(r'(?P<status>BEGIN):VCARD')
    tag = '%(status)s:VCARD'

class end(Component):
    single = True
    pattern = compile(r'(?P<status>END):VCARD')
    tag = '%(status)s:VCARD'

class fn(Component):
    single = True
    pattern = compile(r"""
        N:
          (?P<family>[^;]*);
          (?P<given>[^;]*);
          (?P<additional>[^;]*);
          (?P<prefix>[^;]*);
          (?P<suffix>\S*)
        """, VERBOSE
    )
    tag = 'N:%(family)s;%(given)s;%(additional)s;%(prefix)s;%(suffix)s'

class n(Component):
    single = True
    pattern = compile(r"FN:(?P<full_name>.+)")
    tag = 'FN:%(full_name)s'

class org(Component):
    single = False
    pattern = compile(r"ORG:(?P<organization>.+)")
    tag = 'ORG:%(organization)s'

class tel(Component):
    single = False
    pattern = compile(
        r"TEL;(?:TYPE=(?P<type>[^;]+);)?VALUE=uri:tel:(?P<phone>.+)"
    )
    tag = 'TEL;TYPE=%(type)s:%(phone)s'

    def _convert(self):
        if self.get('type') is None:
            self['type'] = 'WORK,VOICE'
        return

class rev(Component):
    single = True
    pattern = compile(r"""
        REV:
            (?P<year>\d{4})
            (?P<month>\d{2})
            (?P<day>\d{2})
            T
            (?P<hour>\d{2})
            (?P<minute>\d{2})
            (?P<second>\d{2})
            (?P<timezone>\w+)
        """, VERBOSE
    )
    tag = 'REV:%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s%(timezone)s'

class version(Component):
    single = True
    pattern = compile('VERSION:(?P<version>[\d\.]+)')
    tag = 'VERSION:%(version)s'

class email(Component):
    single = False
    pattern = compile('EMAIL:(?P<email>.+)')
    tag = 'EMAIL:%(email)s'

class address(Component):
    single = False
    pattern = compile(r'''
        ADR:
            (?:TYPE=(?P<type>[^;]*))?;
            (?:LABEL=(?P<label>[^;]*))?;
            (?P<street>[^;]*);
            (?P<city>[^;]*);
            (?P<county>[^;]*);
            (?P<postcode>[^;]*);
            (?P<country>[^;]*)
        ''', VERBOSE
    )
    tag = 'ADR:;;%(street)s;%(city)s;%(county)s;%(postcode)s;%(country)s'

    def _convert(self):
        if self.get('type') is None:
            self['type'] = 'HOME'
        return
