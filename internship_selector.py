
# Reading an excel file using Python
import openpyxl
import pandas as pd
from os import devnull
import xlrd
import pprint
loc = ("./APPIC_directory_search_results.xlsx")

wb = openpyxl.load_workbook(loc)

ws = wb.active

ws.auto_filter.ref = "A2:E809"
ws.auto_filter.add_filter_column(0, ["1165", "1254"])
wb.save("filtered.xlsx")
# # iterate through excel and display data
# count = 0
# locations_set = set()
# locations_dict = {}
# for i in range(1, ws.max_row+1):
#     print(ws.row[i])
#     site_name = ws.cell(row=i, column=2)
#     location = ws.cell(row=i, column=4)
#     if 'USA' in location.value and 'MD,' in location.value:
#         count += 1
#         locations_dict.setdefault(location.value, [])
#         locations_dict[location.value] = site_name.value
#         locations_set.add(location.value)
#         # print("\n")
#         # print("Row ", i, " data :")
#         # print(site_name.value)
#         # print("\n")
#         # print(location.value)
# print(count, '/',  ws.max_row+1)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(locations_dict)
# pp.pprint(locations_set)
