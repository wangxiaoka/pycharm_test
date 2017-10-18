import os
import xlrd
from xlutils.copy import copy

index = 0
file = open(os.path.join(os.getcwd(), 'PPG2.txt'), 'r', encoding='utf-8')
excel = xlrd.open_workbook(os.path.join(os.getcwd(), 'data1.xls'), 'r')
rs = excel.sheet_by_index(index)
wb = copy(excel)
ws = wb.get_sheet(index)
line1 = file.readlines()
#print(line1)
for line in line1:
                #print(line + '...' + str(len(line)))
                l = 1
                if 'HR:***' in line:
                    heart = line.strip().split('HR:***')[1].split('***')
                    date = line.strip().split('HR:***')[0].split('***')
                    date11 = date[0].split()
                    heart = heart[0]
                    heart = int(heart)
                    #print(rs.nrows)

                    while l < rs.nrows:
                        print(rs.cell_value(l, 0))
                        #breaker = input("停顿一下")
                        date1 = rs.cell_value(l, 0).split()
                        if date11[1] == date1[1]:
                            ws.write(l, 2, heart)
                            break
                        l += 1




wb.save(os.path.join(os.getcwd(), 'data1.xls'))

wb.save(os.path.join(os.getcwd(), 'data1.xls'))
