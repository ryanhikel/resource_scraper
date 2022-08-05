
# Reading an excel file using Python
import openpyxl
from pprint import pprint
file_location = ("./directory/APPIC_directory_search_results.xlsx")

wb = openpyxl.load_workbook(file_location)

ws = wb.active

ws.auto_filter.ref = "A2:E809"
ws.auto_filter.add_filter_column(0, ["1165", "1254"])
wb.save("./results/filtered.xlsx")

results = {}
for row in ws.iter_rows(min_col=0, max_col=4, min_row=2):
    id, site_name, url, location = [cell.value for cell in row]
    results[id] = {
        'site_name': site_name,
        'url': url,
        'location': location
    }

pprint(results)
