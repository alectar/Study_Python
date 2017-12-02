import urllib
import re


def get_props(s):
    props = {}
    parse = re.compile('^<li><strong>.+:</strong>.+</li>$', re.M)
    lines = parse.findall(s)
    for line in lines:
        line = line[12:-5]
        # print line
        line = line.split(':</strong> ')
        props[line[0]] = line[1]
        # print line
    if 'Formula' in props.keys():
        props['Formula'] = props['Formula'].replace('<sub>', '')
        props['Formula'] = props['Formula'].replace('</sub>', '')
    parse = re.compile('<title>.+</title>')
    text = parse.search(s).group()
    props['Name'] = text[7:-8].lower().replace(' ', '-')

    parse = re.compile('<td align=\"left\">T<sub>boil</sub></td><td class=\"right-nowrap\">[\.\d]+')
    text = parse.findall(s)
    if text:
        props['Boiling Point'] = text[0][63:]

    parse = re.compile('<td align="left">T<sub>c</sub></td><td class="right-nowrap">[\.\d]+')
    text = parse.findall(s)