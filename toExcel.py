import xlwt

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet

f = open('scrape_data.txt', 'r+', encoding="utf8")

data = f.readlines()            # read all lines at once
print(data)

for i in range(len(data)):
  row = data[i].split(",")

  for j in range(len(data)):
    ws.write(i, j, row)         # Write to cell i, j
    break

book.save('Excelfile' + '.xls')
f.close()
