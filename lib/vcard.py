from re import compile, VERBOSE

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
}

def iter_vcard(vcf):
    for line in vcf:
        if line.startswith('BEGIN:VCARD'):
            vcard = {}
        elif line.startswith('END:VCARD'):
            yield vcard
        else:
            for name, pattern in _patterns.iteritems():
                match = pattern.match(line)
                if match:
                    vcard[name] = match.groupdict()
                    break
    return

_tags = {
    'fn': 'FN:%(full_name)s',
    'n': 'N:%(family)s;%(given)s;%(additional)s;%(prefix)s;%(suffix)s',
    'org': 'ORG:%(organization)s',
    'tel': 'TEL;TYPE=%(type)s:%(phone)s',

}

def downgrade(v4card):
    v3card = [
        'START:VCARD',
        'VERSION:3.0',
        'REV:2008-04-24T19:52:43Z',
    ]
    for tag_name, tag_data in v4card.iteritems():
        tag = _tags[tag_name]
        if tag_name in _converters:
            tag_data = _converters[tag_name](tag_data)
        v3card.append(tag % tag_data)
    v3card.append('END:VCARD')
    return '\n'.join(v3card)

_converters = {
}
