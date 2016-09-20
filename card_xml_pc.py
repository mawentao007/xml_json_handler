# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

input_file = "base_xml"
with_reason = "query_with_reason"
without_reason = "query_without_reason"
query_list = []
noquery_list = []
with open("./data/diff.xml", 'r') as xf:
	for line in xf.readlines():
		line = line.decode("gb18030").encode("utf-8")

		node = ET.fromstring(line)
		key = node.find('key').text
		e = node.find("./display/Right_Resources/card/list[0]/attridk")
		if e == None:
			noquery_list.append(key)
		query_list.append(key)

			#print >> sys.stderr,line




with open(with_reason, 'w') as dq:
	for x in query_list:
		dq.write(x.encode("gb18030")+'\n')

with open(without_reason, 'w') as dq:
	for x in noquery_list:
		dq.write(x.encode("gb18030")+'\n')
