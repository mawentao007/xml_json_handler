# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

sid='20991'
input_file = sid+"_all_xml"
with_reason = sid+"query_with_reason"
without_reason = sid+"query_without_reason"
query_list = []
noquery_list = []
with open(input_file, 'r') as xf:
	for line in xf.readlines():
		try:

			line = line.decode("gb18030").encode("utf-8")

			node = ET.fromstring(line)
			key = node.find('key').text
			e = node.find("./display/Right_Resources/card/list[0]/attrid")
			if e == None:
				noquery_list.append(key)
			else:
				query_list.append(key)
		except:
			print >> sys.stderr, line




with open(with_reason, 'w') as dq:
	for x in query_list:
		dq.write(x.encode("gb18030")+'\n')

with open(without_reason, 'w') as dq:
	for x in noquery_list:
		dq.write(x.encode("gb18030")+'\n')
