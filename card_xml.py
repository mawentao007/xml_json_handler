# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""

import codecs

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

base_xml_file = "./data/test_12793"
expr_xml_file = "./data/test_19190"
base_dic = {}
expr_dic = {}
query_only_expr = []
diff_query = []
diff_query_file= "diff_query"
only_expr_file= "only_expr"
with open(base_xml_file, 'r') as xf:
	for line in xf.readlines():
		line = line.decode("gb18030").encode("utf-8")
		try:
			entities = []
			node = ET.fromstring(line)
			key = node.find('key').text
			for e in node.findall(".//name"):            #选择所有子节点
				entities.append(e.text)
			base_dic[key] = entities
		except:
			print line + "error"


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
			print line

for (k,v) in expr_dic.iteritems():
	if k not in base_dic:
		print k + " only expr"
		query_only_expr.append(k)
	if v != base_dic[k]:
		print k + " diff"
		diff_query.append(k)






