from re import compile, VERBOSE
from collections import OrderedDict

_patterns = {
    'n': compile(r"""
        N:
          (?P<family>[^;]*);
          (?P<given>[^;]*);
          (?P<additional>[^;]*);
          (?P<prefix>[^;]*);
          (?P<suffix>\S*)
        """, VERBOSE
    ),
    'fn': compile(r"FN:(?P<full_name>.+)"),
    'org': compile(r"ORG:(?P<organization>.+)"),
    'tel': compile(
        r"TEL;(TYPE=(?P<type>[^;]+);)?VALUE=uri:tel:(?P<phone>.+)"
     ),
     'rev': compile(r"""
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
     ),
     'version': compile('VERSION:(?P<version>[\d\.]+)'),
     'email': compile('EMAIL:(?P<email>.+)')
}

def build_v4card(vcf):
    v4card = OrderedDict()
    for line in vcf:
        for name, pattern in _patterns.iteritems():
            match = pattern.match(line)
            if match:
                contents = v4card.setdefault(name, [])
                contents.append(match.groupdict())
                break
    return v4card

def iter_vcard(vcf):
    vcard = []
    for line in vcf:
        if line.startswith('BEGIN:VCARD'):
            vcard = [line]
        else:
            vcard.append(line)
        if line.startswith('END:VCARD'):
            yield vcard
    return


_tags = {
    'fn': 'FN:%(full_name)s',
    'n': 'N:%(family)s;%(given)s;%(additional)s;%(prefix)s;%(suffix)s',
    'org': 'ORG:%(organization)s',
    'tel': 'TEL;TYPE=%(type)s:%(phone)s',
    'rev': 'REV:%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s%(timezone)s',
    'version': 'VERSION:%(version)s',
    'email': 'EMAIL:%(email)s'
}

def downgrade(v4card):
    v3card = [
        'BEGIN:VCARD',
    ]
    for name, contents in v4card.iteritems():
        tag = _tags[name]
        for content in contents:
            if name in _converters:
                converter = _converters[name]
                content = converter(content)
            v3card.append(tag % content)
    v3card.append('END:VCARD')
    return '\n'.join(v3card)

def _version(data):
    return {'version': '3.0'}

def _tel(data):
    _data = data.copy()
    if _data.get('type') is None:
        _data['type'] = 'WORK,VOICE'
    return _data

_converters = {
    'version': _version,
    'tel': _tel,
}

