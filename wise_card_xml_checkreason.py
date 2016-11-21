# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
    print "usage: xml_file"
    sys.exit(1)

xml_file = sys.argv[1]

reason_query = set()




with open(xml_file, 'r') as xf:
    for line in xf.readlines():
        line = line.decode("gb18030").encode("utf-8")
        try:
            node = ET.fromstring(line)
            key = node.find('key').text
            for e in node.findall(".//type"):          
                if e.text != "relation" and e.text !=None:
                    reason_query.add(key)
                    break
        except:
            #pass
            print >> sys.stderr,line




with open("reason_query", 'w') as nf:
    for x in reason_query:
        nf.write(x.encode("gb18030")+'\n')
