# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:33:31 2019

@author: admin
"""

### Excel文件 ###
# xlrd、xlwt

## 内省Excel工作表 ##
from xlrd import open_workbook

input_file = 'sales_2013.xlsx'

# open_workbook()函数打开一个Excel文件，并赋给一个workbook对象
workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
# workbook对象的sheets方法可以识别出所有工作表
for worksheet in workbook.sheets():
    # worksheet对象的name属性来确定每个工作表的名称，nrows与ncols属性确定每个工作表中行与列的数量
    print('Worksheet name:', worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
    

## 处理单个工作表 ##
# 读写Excel文件 #
from xlrd import open_workbook
# 导入xlwt模块的Workbook对象
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'

# 实例化一个xlwt的workbook对象
output_workbook = Workbook()
# 为输出工作簿添加一个工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    # 使用workbook对象的sheet_by_name函数引用名称为january_2013的工作表
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            output_worksheet.write(row_index, col_index, worksheet.cell_value(row_index, col_index))
output_workbook.save(output_file)
# 结果将日期保存为浮点数，代表从1900年经过的日期数加上一个24小时的小数部分

# 格式化日期数据
from datetime import date
# xldate_as_tuple可以将Excel中代表日期、时间或日期时间的数值转换为元组，只要将数值转为元组就可以提取出具体时间元素
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            # 单元格类型为3表示这个单元格中包含日期数据
            if worksheet.cell_type(row_index, col_index) == 3:
                # cell_value函数和行列索引来引用单元格中的值，还可以使用cell().value函数
                # 参数workbook.datemode是必须的，可以使函数确定日期是基于1900年还是基于1904年，并根据此将数值转换成正确的元组
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)
                # strftime函数将date对象转换为一个具有特定格式的字符串
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)                
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, sheetname='january_2013')
writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='jan_13_output', index = False)
writer.save()

## 筛选特定行 ##
# 行中的值满足某个条件
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
sale_amount_column_index = 3

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    date = []
    header = worksheet.row_values(0)
    date.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)
        if sale_amount > 1400.0:
            for col_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, col_index)
                cell_type = worksheet.cell_type(row_index, col_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    # 此处报错：TypeError: 'list' object is not callable
                    date_cell = date(date_cell[0], date_cell[1], date_cell[2]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(date):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)       

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]
writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name = 'jan_13_output', index = False)
writer.save()


# 行中的值属于某个集合 #
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
important_dates = ['01/24/2013', '01/31/2013']
purchase_date_column_index = 4

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_column_index), workbook.datemode)
        purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
        row_list = []
        if purchase_date in important_dates:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                    print('date_cell: ' + date_cell)
                else:
                    row_list.append(cell_value)
                    print('cell_value: ' + str(cell_value))
    if row_list:
        data.append(row_list)
    # data中包含两个list
    print(data)
# list_index为data中第几个列表，output_list为第k个列表中的索引值
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
        print(list_index, element_index, element)
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
important_dates = ['01/24/2013','01/31/2013']
data_frame_value_in_set = data_frame[data_frame['Purchase Date']\
.isin(important_dates)]
writer = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()


# 行中的值匹配于特定模式 #
import re
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# r表示单引号之间的模式是一个原始字符串， 插入符号^表示在字符串开头搜索模式
# 句点.可以匹配除换行符外的任何字符，*表示重复前面的字符0次或更多次
pattern = re.compile(r'(?P<my_pattern>^I.*)')
customer_name_column_index = 1

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                    print('date_cell: ' + date_cell)
                else:
                    row_list.append(cell_value)
                    print('cell_value: ' + str(cell_value))
    if row_list:
        data.append(row_list)
    # data中包含两个list
    print(data)
# list_index为data中第几个列表，output_list为第k个列表中的索引值
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
        print(list_index, element_index, element)
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith("J")]
writer = pd.ExcelWrite22r(output_file)
data_frame_value_matches_pattern.to_excel(writer, sheet_name = 'jan_13_output', index=False)
writer.save()


# 选取特定列 #
# 列索引值
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
my_column = [1, 4]

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    for row_index in range(1, worksheet.nrows):
        row_list = []
        for column_index in my_column:
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                    print('date_cell: ' + date_cell)
                else:
                    row_list.append(cell_value)
                    print('cell_value: ' + str(cell_value))
        data.append(row_list)
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
        print(list_index, element_index, element)
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_column_by_index = data_frame.iloc[:, [1, 4]]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer,  sheet_name = 'jan_13_output', index=False)
writer.save()

# 列标题
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
my_columns = ['Customer ID', 'Purchase Date']

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header_list = worksheet.row_values(0)
    header_index_list = []
    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)
    for row_index in range(1, worksheet.nrows):
        row_list = []
        for column_index in header_index_list:
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                    print('date_cell: ' + date_cell)
                else:
                    row_list.append(cell_value)
                    print('cell_value: ' + str(cell_value))
        data.append(row_list)
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
        print(list_index, element_index, element)
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_column_by_index = data_frame.loc[:, ['Customer ID', 'Purchase Date']]
writer = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(writer,  sheet_name = 'jan_13_output', index=False)
writer.save()


## 读取工作簿中的所有工作表 ##
# 在所有工作表中筛选特定行
# 销售额>2000
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cp.xlsx'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_worksheets')
sales_column_index = 3
threshold = 2000.0
first_worksheet = True
with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = []
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_list.append(date_cell)
                        print('date_cell: ' + date_cell)
                    else:
                        row_list.append(cell_value)
                        print('cell_value: ' + str(cell_value))
        if row_list:
            data.append(row_list)
            print(data)
for list_index, output_list in enumerate(data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
        print(list_index, element_index, element)
output_workbook.save(output_file)

# pandas
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, sheetname = None, index_col = None)
row_output = []
for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis = 0, ignore_index = True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name = 'sale_amount_gt2000', index = False)
writer.save()

# 在所有工作表中选取特定列
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'

data_frame = pd.read_excel(input_file, sheetname = None, index_col = None)
print(type(data_frame))
column_output = []
for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])
selected_columns = pd.concat(column_output, axis = 0, ignore_index = True)
writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name = 'selected_columns_all_worksheets', index = False)
writer.save()


## 在Excel工作簿中读取一组工作表
# 在一组工作表中筛选特定行
import pandas as pd

input_file = 'sales_2013.xlsx'
output_file = 'sales_2013_cpp.xlsx'
my_sheets = [0, 1]
threshold = 1900.0

data_frame = pd.read_excel(input_file, sheetname = my_sheets, index_col = None)
row_list = []
for worksheet_name, data in data_frame.items():
    row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_rows = pd.concat(row_list, axis=0, ignore_index = True)
writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name = 'set_of_worksheets', index = False)
writer.save()


## 处理多个工作簿 ##
# 工作表技术及每个工作表中的行列计数
import glob
import os
from xlrd import open_workbook
input_path = "D:\proexc\python\sjfxjc\sales"
workbook_counter = 0
for input_file in glob.glob(os.path.join(input_path, '*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook: %s' % os.path.basename(input_file))
    print('Number of worksheets: %d' % workbook.nsheets)
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, '\tRows:', worksheet.nrows, '\tColumns:', worksheet.ncols)
    workbook_counter += 1
print('Number of Excel workbooks: %d' % (workbook_counter))

# 从多个工作簿中连接数据 #
import pandas as pd
import glob
import os 

input_path = "D:\proexc\python\sjfxjc\sales"
output_file = "sales_cpp.xlsx"

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheetname = None, index_col = None)
    for worksheet_name, data in all_worksheets.items():
        data_frames.append(data)
all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index = True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='all_data_all_workbooks', index = False)
writer.save()

# 为每个工作簿和工作表计算总数和均值 #
import pandas as pd
import glob
import os 

input_path = "D:\proexc\python\sjfxjc\sales"
output_file = "sales_cpp.xlsx"

all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = []

for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheetname = None, index_col = None)
    workbook_total_sales = []
    workbook_number_of_sales = []
    worksheet_data_frames = []
    worksheets_data_frame = None
    workbook_data_frame = None
    for worksheet_name, data in all_worksheets.items():
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data.loc[:, 'Sale Amount']]).sum()
        print("total sales: " + str(total_sales))
        number_of_sales = len(data.loc[:, 'Sale Amount'])
        average_sales = pd.DataFrame(total_sales / number_of_sales)
        
        workbook_total_sales.append(total_sales)
        workbook_number_of_sales.append(number_of_sales)
        
        data = {'workbook': os.path.basename(workbook),
                'worksheet': worksheet_name,
                'worksheet_total': total_sales,
                'worksheet_average': average_sales}
        
        worksheet_data_frames.append(pd.DataFrame(data, columns = ['workbook', 'worksheet', \
                                    'worksheet_total', 'worksheet_average']))
    worksheet_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True)
    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
    workbook_average = pd.DataFrame(workbook_total / workbook_total_number_of_sales)

    workbook_stats = {'workbook': os.path.basename(workbook),'workbook_total': workbook_total,
                      'workbook_average': workbook_average}
    print(workbook_stats)
    workbook_stats = pd.DataFrame(workbook_stats, columns=['workbook', 'workbook_total', 'workbook_average'])
    workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, \
                                    on='workbook', how='left')
    data_frames.append(workbook_data_frame)
all_data_concatenated = pd.concat(data_frames, axis=0, ignored_index=True)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='sums_and_averages', index=False)
writer.save()

















