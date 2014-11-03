from sys import stderr
from collections import OrderedDict

from component import factory, version, InvalidTag

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

class vCard(OrderedDict):
    @classmethod
    def from_lines(cls, lines):
        self = cls()
        for line in lines:
            try:
                self.add(line)
            except InvalidTag, error:
                print >> stderr, line
        return self

    def add(self, line):
        Component = factory(line)
        component = Component(line)
        if Component.single:
            self[Component] = component
        else:
            self.setdefault(Component, []).append(component)
        return

    def downgrade(self):
        v3card = vCard(self.copy())
        v3card[version] = version('VERSION:3.0')
        lines = [component.dump() for component in v3card.iter_components()]
        return '\n'.join(lines)

    def iter_components(self):
        for Component, components in self.iteritems():
            if Component.single:
                yield components
            else:
                for component in components:
                    yield component
        return

