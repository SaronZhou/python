# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:09:59 2019

@author: admin
"""

# 在一个大文件集合中查找一组项目 #
#!/usr/bin/env python3
import sys
import csv
import glob
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple

item_numbers_file = "item_numbers_to_find.csv"
path_to_folder = "D:\proexc\python\sjfxjc\sales"
output_file = "chap5_output1.csv"


item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
	filereader = csv.reader(item_numbers_csv_file)
	for row in filereader:
		item_numbers_to_find.append(row[0])
print(item_numbers_to_find)

filewriter = csv.writer(open(output_file, 'a', newline=''))

file_counter = 0
line_counter = 0
count_of_item_numbers = 0
for input_file in glob.glob(os.path.join(path_to_folder, 'suppliers*.*')):
	file_counter += 1
    # 将每个输入文件按照路径名中的句点进行分割，前半部分索引为0，后半部分索引为1
	if input_file.split('.')[1] == 'csv':
		with open(input_file, 'r', newline='') as csv_in_file:
			filereader = csv.reader(csv_in_file)
			header = next(filereader)
			for row in filereader:
				row_of_output = []
				for column in range(len(header)):
					if column < 3:
						cell_value = str(row[column]).strip()
						row_of_output.append(cell_value)
					elif column == 3:
						cell_value = str(row[column]).lstrip('$').replace(',','').split('.')[0].strip()
						row_of_output.append(cell_value)
					else:
						cell_value = str(row[column]).strip()
						row_of_output.append(cell_value)
				row_of_output.append(os.path.basename(input_file))
				if row[0] in item_numbers_to_find:
					filewriter.writerow(row_of_output)
					count_of_item_numbers += 1
				line_counter += 1
	elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
		workbook = open_workbook(input_file)
		for worksheet in workbook.sheets():
			try:
				header = worksheet.row_values(0)
			except IndexError:
				pass
			for row in range(1, worksheet.nrows):
				row_of_output = []
				for column in range(len(header)):
					if column < 3:
						cell_value = str(worksheet.cell_value(row,column)).strip()
						row_of_output.append(cell_value)
					elif column == 3:
						cell_value = str(worksheet.cell_value(row,column)).split('.')[0].strip()
						row_of_output.append(cell_value)
					else:
						cell_value = xldate_as_tuple(worksheet.cell(row,column).value,workbook.datemode)
						cell_value = str(date(*cell_value[0:3])).strip()
						row_of_output.append(cell_value)
				row_of_output.append(os.path.basename(input_file))
				row_of_output.append(worksheet.name)
				if str(worksheet.cell(row,0).value).split('.')[0].strip() in item_numbers_to_find:
					filewriter.writerow(row_of_output)
					count_of_item_numbers += 1
				line_counter += 1
print('Number of files: {}'.format(file_counter))
print('Number of lines: {}'.format(line_counter))
print('Number of item numbers: {}'.format(count_of_item_numbers))


# 为csv文件中数据的任意数目分类计算统计量 #
import csv
from datetime import date, datetime

def date_diff(date1, date2):
    try:
        diff = str(datetime.strptime(date1, '%m/%d/%Y') - datetime.strptime(date2, '%m/%d/%Y')).split()[0]
    except:
        diff = 0
    if diff == '0:00:00':
        diff = 0
    return diff
    
input_file = 'customer_category_history.csv'
output_file = 'chap5_output2.csv'
packages = {}
first_row = True
previous_name = 'N/A'
previous_package = 'N/A'
previous_package_date = 'N/A'
today = date.today().strftime('%m%d%Y')

with open(input_file, 'r', newline='') as input_csv_file:
    filereader = csv.reader(input_csv_file)
    header = next(filereader)
    for row in filereader:
        current_name = row[0]
        current_package = row[1]
        current_package_date = row[3]
        if current_name not in packages:
            packages[current_name] = { }
        if current_package not in packages[current_name]:
            packages[current_name][current_package] = 0
        if current_name != previous_name:
            if first_row:
                first_row = False
            else:
                diff = date_diff(today, previous_package_date)
                if previous_package not in packages[previous_name]:
                    packages[previous_name][previous_package] = int(diff)
                else:
                    packages[previous_name][previous_package] += int(diff)
        else:
            diff = date_diff(current_package_date, previous_package_date)
            packages[previous_name][previous_package] = int(diff)
        previous_name = current_name
        previous_package = current_package
        previous_package_date = current_package_date
header = ['Customer Name', 'Category', 'Total Time (in Days)']
with open(output_file, 'w', newline='') as output_csv_file:
    filewriter = csv.writer(output_csv_file)
    filewriter.writerow(header)
    for customer_name, customer_name_value in packages.items():
        for package_category, package_category_value in packages[customer_name].items():
            row_of_output = []
            print(customer_name, package_category, package_category_value)
            row_of_output.append(customer_name)
            row_of_output.append(package_category)
            row_of_output.append(package_category_value)
            filewriter.writerow(row_of_output)
            
            
            
            
            