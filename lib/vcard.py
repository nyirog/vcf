from vobject import readOne, vCard

def iter_vcard(vcf):
    for line in vcf:
        if line.startswith('BEGIN:VCARD'):
            lines = [line]
        else:
            lines.append(line)
        if line.startswith('END:VCARD'):
            yield readOne('\n'.join(lines))
    return

def downgrade(v4card):
    v3card = vCard()
    version = v3card.add('version')
    version.value = '3.0'

    rev = v3card.add('rev')
    rev.value = '2008-04-24T19:52:43Z'

    for name, values in v4card.contents.iteritems():
        if name in ('version', 'rev'):
            continue
        value = values[0].value
        if name == 'tel':
            value = value.split(':')[1]
        content = v3card.add(name)
        content.value = value
    return v3card

