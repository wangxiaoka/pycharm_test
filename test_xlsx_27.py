# -*- coding: utf-8 -*-
import datetime
import glob
import os
import xlrd
import xlwt
import xlsxwriter
from xlutils.copy import copy



######读取待测试点表格
path = 'E:\迅雷下载'
file = 'HMPCB_TEST.xlsx'
Path = os.path.join(path,file)
print (Path)
Path = Path.decode('utf8').encode('gbk')
print (Path)
excel_t = xlrd.open_workbook(Path,'wb')
#excel_t = xlrd.open_workbook(os.path.join(os.getcwd(),'HMPCB_TEST.xlsx'),'wb')
worksheet_t = excel_t.sheet_by_name(u'NIHAO')

num_rows_t = worksheet_t.nrows
for curr_row_t in range(num_rows_t):
	row_t = worksheet_t.row_values(curr_row_t)
	#print('row_t%s is %s' % (curr_row_t, row_t))

num_cols_t = worksheet_t.ncols
for curr_col_t in range(num_cols_t):
	col_t = worksheet_t.col_values(curr_col_t)
	#print('col_t%s is %s' %(curr_col_t,col_t))

######读取待测试点表格
path_lib = 'E:\迅雷下载'
file_lib = 'HMPCB.xlsx'
Path_lib = os.path.join(path_lib,file_lib)
print (Path_lib)
Path_lib = Path_lib.decode('utf-8').encode('gbk')
excel_h = xlrd.open_workbook(Path_lib,'wb')

#excel_h = xlrd.open_workbook(os.path.join(os.getcwd(),'HMPCB.xlsx'),'wb')
worksheet_h = excel_h.sheet_by_name(u'Sheet1')

num_rows_h = worksheet_h.nrows
for curr_row_h in range(num_rows_h):
	row_h = worksheet_h.row_values(curr_row_h)
	#print('row_h%s is %s' % (curr_row_h, row_h))

num_cols_h = worksheet_h.ncols
for curr_col_h in range(num_cols_h):
	col_h = worksheet_h.col_values(curr_col_h)
	#print('col_h%s is %s' %(curr_col_h,col_h))


for rown_t in range(num_rows_t-1):
	cell_t = worksheet_t.cell_value(rown_t+1,0)
	#print cell_t
	for rown_h in range(num_rows_h-1):
		cell_h = worksheet_h.cell_value(rown_h+1,0)
		#print cell_h + '--' + cell_t
		if str(cell_t) == str(cell_h):
			xsize = worksheet_h.cell_value(rown_h+1,1)
			ysize = worksheet_h.cell_value(rown_h+1,2)
			print ('%s坐标是%s %s' %(str(cell_h),str(int(xsize)),str(int(ysize))))
			break
		else:
			continue
		#print ('%s行 %s列 is ' %(rown + 1,coln + 1) + str(cell))




