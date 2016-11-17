# coding=utf-8
"""

 Created by mawentao on 16/9/18.

"""
import sys

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

if len(sys.argv) < 4:
	print "usage:\tbase_xml\texpr_xml\t[1|2]"
	sys.exit(1)

base_xml_file = sys.argv[1]
expr_xml_file = sys.argv[2]
card = sys.argv[3]

base_dic = {}
expr_dic = {}

query_only_expr = []
diff_query = []
nodiff_query = []

diff_query_file= "diff_query_" + card
only_expr_file= "only_expr_" + card
nodiff_file = "nodiff_query_" + card
query_base = "query_base_" + card
query_expr = "query_expr_" + card


with open(base_xml_file, 'r') as xf:
	for line in xf.readlines():
		line = line.decode("gb18030").encode("utf-8")
		try:
			entities = []
			node = ET.fromstring(line)
			key = node.find('key').text
			num = 0
			for e in node.findall(".//name"):          
				if num > 4:
					break
				entities.append(e.text)
				num += 1
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
			num = 0
			for e in node.findall('.//name'):
				if num > 4:
					break
				entities.append(e.text)
				num += 1
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


print "only expr:\t" + str(len(query_only_expr))
print "diff query:\t" + str(len(diff_query))
print "nodiff query:\t" + str(len(nodiff_query))
print "base query:\t" + str(len(base_dic))
print "expr query:\t" + str(len(expr_dic))

with open(query_base, 'w') as qb:
	for x in base_dic.keys():
		qb.write(x.encode("gb18030")+'\n')
	
with open(query_expr, 'w') as qe:
	for x in expr_dic.keys():
		qe.write(x.encode("gb18030")+'\n')

with open(diff_query_file, 'w') as dq:
	for x in diff_query:
		dq.write(x.encode("gb18030")+'\n')

with open(only_expr_file, 'w') as dq:
	for x in query_only_expr:
		dq.write(x.encode("gb18030")+'\n')

with open(nodiff_file, 'w') as nf:
	for x in nodiff_query:
		nf.write(x.encode("gb18030")+'\n')
