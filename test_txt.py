# -*- coding: utf-8 -*-
import glob
import xlwt
import xlrd
import xlsxwriter
import os
import math
from xlutils.copy import copy

def garmin_process(filename, path):
	try:
		file = open(filename, 'r', encoding='utf-8')
		line = file.readlines()
		excel = xlrd.open_workbook("%s.xls" % path)
		wb = copy(excel)
		ws = wb.get_sheet(0)
		ws.write(0, 0, "count")
		ws.write(0, 1, "heart")
		ws.write(0, 2, "spm")
		ws.write(0, 3, "stepcandence")
		ws.write(0, 4, "lation_x")
		ws.write(0, 5, "lation_y")
		for line1 in line:
			list = line1.strip().split(':')
			list1 = list[1].strip('[').strip(']').split(', ')
			length = len(list1)
			if list[0] == 'garmin_data':
				continue
			elif list[0] == "count":
				for i in range(length):
					ws.write(i+1, 0, str(round(float(list1[i]))))
			elif list[0] == "heart":
				for i in range(length):
					ws.write(i+1, 1, str(round(float(list1[i]))))
			elif list[0] == "spm":
				for i in range(length):
					ws.write(i+1, 2, str(round(float(list1[i]),2)))
			elif list[0] == "stepcandence":
				for i in range(length):
					ws.write(i+1, 3, str(round(float(list1[i]),2)))
			elif list[0] == "latlon":
				for i in range(int(length/2)):
					list1_1 = list1[2*i].strip('[')
					ws.write(i+1, 4, list1_1)
					list1_2 = list1[2*i+1].strip(']')
					ws.write(i+1, 5, list1_2)
			else:
				break

		wb.save("%s.xls" % path)

	except Exception as e:
		print(e)

def run():
	file = glob.glob("garmin*.log")
	path = "data_process"
	workbook = xlsxwriter.Workbook('%s.xls' % path)
	workbook.close()
	garmin_process(file[0],path)
	print("执行完毕！！！")

if __name__ == "__main__":
	run()





