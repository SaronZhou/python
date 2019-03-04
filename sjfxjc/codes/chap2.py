# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:19:06 2019

@author: admin
"""



file_path = "tips.csv"
with open(file_path) as f_obj:
    lines = f_obj.readlines()
    
for line in lines:
    print(line.strip())

# delimiter指定默认分隔符，若输入和输出文件都是逗号分隔，就无需指定参数
import csv

input_file = "tips.csv"
output_file = "tips_cp.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)
    
# pandas模块
import pandas as pd

data_frame = pd.read_csv("tips.csv")
print(data_frame)

## 筛选特定的行 ##
# 行中的值满足某个条件
import csv

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # next函数读出输入文件的第一行
        header = next(filereader)
        # 将标题行写入输出文件
        filewriter.writerow(header)
        for row_list in filereader:
            # row_list[0]：读出每行供应商的名字
            supplier = str(row_list[0]).strip()
            # 读出每行数据的成本，删除美元符号，删除逗号
            cost = str(row_list[3]).strip('$').replace(',', '')
            if supplier == 'Supplier Z' or float(cost) > 600.0:       
                print(row_list)
                filewriter.writerow(row_list)
                
# pandas
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').replace(',', '').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) |
        (data_frame['Cost'] > 600), :]
data_frame_value_meets_condition.to_csv(output_file, index = False)

# 行中的值属于某个集合
import csv

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"
important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # next函数读出输入文件的第一行
        header = next(filereader)
        # 将标题行写入输出文件
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)

# pandas——iloc
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"
important_dates = ['1/20/14', '1/30/14']

data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index = False)

# 行中的值匹配于某个模式/正则表达式
import csv
import re

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"
# 符号*表示只在字符串开头搜索模式，句点.除了换行符外可以匹配任意字符，*表示重复前面的字符0次或更多次
pattern = re.compile(r'("?P<my_pattern_group>^001-.*)', re.I)
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # next函数读出输入文件的第一行
        header = next(filereader)
        # 将标题行写入输出文件
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)

# pandas
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file, index = False)


## 选取特定的列 ##
# 列索引值
import csv

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"
my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = [ ]
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)

# pandas
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_column_by_index.to_csv(output_file, index = False)

# 列标题
import csv

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"
my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # 使用next函数读出文件第一行
        header = next(filereader, None)
        for index_value in range(len(header)):
            # index_value从0开始
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        for row_list in filereader:
            row_list_output = [ ]
            for index_value in my_columns_index:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)

# pandas——loc
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index = False)


## 选取连续的行 ##
import csv

input_file = "supplier_data_unnecessary.csv"
output_file = "supplier_data_cp.csv"
row_counter = 0

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            if row_counter >=3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row_list])
            row_counter += 1
            
# pandas——drop函数根据航索引或列标题来丢弃行或列
#       ——iloc函数根据行索引选取一个单独行作为列索引
#       ——reindex函数为数据框重新生成索引
import pandas as pd

input_file = "supplier_data_unnecessary.csv"
output_file = "supplier_data_cpp.csv"

data_frame = pd.read_csv(input_file, header = None)
data_frame = data_frame.drop([0,1,2,16,17,18])
# df.columns重命名列名
# s.iloc[0]：按位置选取数据  s.loc['index_one']：按索引选取数据
data_frame.columns = data_frame.iloc[0]
# 删除标题行，创建新索引
data_frame = data_frame.reindex(data_frame.index.drop(3))
data_frame.to_csv(output_file, index = False)


          
## 添加标题行 ##
import csv

input_file = "supplier_data.csv"
output_file = "supplier_data_cp.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)

# pandas
import pandas as pd

input_file = "supplier_data.csv"
output_file = "supplier_data_cpp.csv"
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']

data_frame = pd.read_csv(input_file, header = None, names = header_list)
data_frame.to_csv(output_file, index = False)

## 读取多个csv文件
import csv
# glob模块可以定位匹配于某个特定模式的所有路径名
import glob
# os模块包含了用于解析路径名的函数，os.path.basename(path)返回path的基本文件名
import os

input_path = "D:\proexc\python\sjfxjc"
file_counter = 0

# os.path.join将函数圆括号中的两部分连接在一起
# glob.glob()函数将'sales_*'中的*转换为实际的文件名
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
            
            
## 从多个文件中连接数据 ##
import csv
import glob
import os
           
input_path = "D:\proexc\python\sjfxjc"
output_file = 'sales_2014_cp.csv'

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline = '') as csv_in_file:
        # 以追加方式打开文件
        with open(output_file, 'a', newline = '') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                # next方法将每个文件中的标题赋给一个变量，这样就可以在后面的处理中跳过标题行
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)
            
# pandas
# concat函数可以使用axis参数来设置连接数据框的方式，axis=0表示从头到尾垂直堆叠，axis=1表示并排平行堆叠
import pandas as pd
import glob
import os

input_path = "D:\proexc\python\sjfxjc"
output_file = 'sales_2014_cpp.csv'
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for file in all_files:
    data_frame = pd.read_csv(file, index_col = None)
    all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index = True)
data_frame_concat.to_csv(output_file, index = False)             
  
          
## 计算每个文件中值的总和与均值 ##
import csv
import glob
import os

input_path = "D:\proexc\python\sjfxjc"
output_file = 'sales_2014_cp.csv'           
output_header_list =  ['file_name', 'total_sales', 'average_sales']
csv_out_file = open(output_file, 'a', newline='')

filewriter = csv.writer(csv_out_file)
# 将标题行写入输出文件
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = [ ]
        output_list.append(os.path.basename(input_file))
        # 使用 next 函数除去每个输入文件的标题行
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        for row in filereader:
            sale_amount = row[3]
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            number_of_sales += 1
        average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()

# pandas
import pandas as pd
import glob
import os

input_path = "D:\proexc\python\sjfxjc"
output_file = 'sales_2014_cpp.csv'
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []
for input_file in all_files:
    filereader = pd.read_csv(input_file, index_col=None)
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) 
                for value in data_frame.loc[:, 'Sale Amount']]).sum()
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))
                for value in data_frame.loc[:, 'Sale Amount']]).mean()
    data = {'file_name': os.path.basename(input_file),\
            'total_sales': total_cost, 'average_sales': average_cost}   
    all_data_frames.append(pd.DataFrame(data, 
            columns=(['file_name', 'total_sales', 'average_sales'])))
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index = False)            
            
            
            
            
            
            
            
            
            
            
            
            