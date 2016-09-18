# coding=utf-8
"""

 Created by mawentao on 16/9/16.

"""

import json
import sys
import re

#file = "diff_part.json"
file = "new_diff_compare_plain"
diff_query_final = "diff_query_final"

error_pair = []
all_key = []
with open(file) as dj:
	all_lines = dj.readlines()
	lines_num = len(all_lines)

	while lines_num > 0:
		try:
			base = all_lines[lines_num-1]
			expr = all_lines[lines_num-2]
			lines_num -= 2

			items_base = base.strip().split("\t")
			key = items_base[0]

			base_json = json.loads(items_base[1], encoding="gb18030")
			#推荐实体 list
			base_entities = base_json["card_list"][0].values()[0][1].values()[0]
			base_entities_length = len(base_entities)
			if base_entities_length < 12:
				all_key.append(key.decode("gb18030"))
				continue
			base_entities_12 = base_entities[:11]

			items_expr = expr.strip().split("\t")
			key = items_expr[0]
			expr_json = json.loads(items_expr[1], encoding="gb18030")
			# 推荐实体 list
			expr_entities = expr_json["card_list"][0].values()[0][1].values()[0]
			expr_entities_length = len(expr_entities)
			expr_entities_12 = expr_entities[0:11]
			if expr_entities_12 != base_entities_12:
				all_key.append(key.decode("gb18030"))
		except ZeroDivisionError:
			print("division by zero!")
		except :
			error_pair.append(key.decode("gb18030"))
			print("Unexpected error:", sys.exc_info()[0])
all_key += error_pair

with open(diff_query_final, "w") as dqf:
	for x in all_key:
		result = re.match(r"\[\"(.*)\".*\]", x)
		dqf.write(result.groups()[0].encode("gb18030") + "\n")





