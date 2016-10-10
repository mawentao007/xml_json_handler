# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

base_xml_file = sys.argv[1]
expr_xml_file = sys.argv[2]

base_dic = {}
expr_dic = {}
query_only_expr = []
diff_query = []
nodiff_query = []

diff_query_file= "diff_query"
only_expr_file= "only_expr"
nodiff_file = "nodiff_query"

with open(base_xml_file, 'r') as xf:
	for line in xf.readlines():
		line = line.decode("gb18030").encode("utf-8")
		try:
			entities = []
			node = ET.fromstring(line)
			key = node.find('key').text
			for e in node.findall(".//name"):          
				entities.append(e.text)
			base_dic[key] = entities
		except:
			pass
			#print >> sys.stderr,line


with open(expr_xml_file, 'r') as xf:
	for line in xf.readlines():
		line = line.decode("gb18030").encode("utf-8")
		entities = []
		try:
			node = ET.fromstring(line)
			key = node.find('key').text
			for e in node.findall('.//name'):
				entities.append(e.text)
			expr_dic[key] = entities
		except:
			pass
			#print >> sys.stderr,line

for (k,v) in expr_dic.iteritems():
	if k not in base_dic:
		query_only_expr.append(k)
	elif v != base_dic[k]:
		diff_query.append(k)
	else:
		nodiff_query.append(k)

print len(query_only_expr)
print len(diff_query)
with open(diff_query_file, 'w') as dq:
	for x in diff_query:
		dq.write(x.encode("gb18030")+'\n')



with open(only_expr_file, 'w') as dq:
	for x in query_only_expr:
		dq.write(x.encode("gb18030")+'\n')

with open(nodiff_file, 'w') as nf:
	for x in nodiff_query:
		nf.write(x.encode("gb18030")+'\n')
