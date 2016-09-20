# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

#base_xml_file = "12793_xml_card2"
#expr_xml_file = "19190_xml_card2"
base_xml_file = "30355_xml_base"
expr_xml_file = "30356_xml_expr"

#base_xml_file = "12793"
#expr_xml_file = "19190"
base_dic = {}
expr_dic = {}
query_only_expr = []
diff_query = []
#diff_query_file= "diff_query_card2"
#only_expr_file= "only_expr_card2"
diff_query_file= "diff_query_card1"
only_expr_file= "only_expr_card1"
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

print len(query_only_expr)
print len(diff_query)
with open(diff_query_file, 'w') as dq:
	for x in diff_query:
		dq.write(x.encode("gb18030")+'\n')



with open(only_expr_file, 'w') as dq:
	for x in query_only_expr:
		dq.write(x.encode("gb18030")+'\n')
