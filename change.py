import csv
import os
import numpy as np

test_path = 'test2.csv'

with open(test_path, mode='r') as f:
    reader = csv.reader(f)
    reader_list = list(reader)
    # print(list(reader))
    filename_list = [filename[0] for filename in reader_list]
    # print(filename_list)

file_list = []
for x in filename_list:
    if x not in file_list:
        file_list.append(x)

filename_array = np.array(filename_list)
reader_array = np.array(reader_list)
result_list = []

for filename in file_list:
    file_info = reader_array[filename_array == filename]
    result_list.append(file_info)

string_list=[]
for result in result_list:
    # string_temp = result[0][0][6:]
    string_temp = result[0][0]
    print(string_temp)
    for x in result[:4]:
        if len(x) == 1:
            break
        string_temp += ' '+x[1][:3]
        string_temp += ' '+x[2]
        string_temp += ' '+x[3]
        string_temp += ' '+x[4]
        string_temp += ' '+x[5]
    # string_temp = string_temp.replace('.jpg ', '.jpg,')
    string_temp = string_temp.replace('.jpg', '.jpg,')
    string_temp = string_temp.replace(', ', ',')
    # string_temp = string_temp.replace(' 2.', '.')
    string_temp = string_temp.replace('D00', '1')
    string_temp = string_temp.replace('D01', '1')
    string_temp = string_temp.replace('D10', '2')
    string_temp = string_temp.replace('D11', '2')
    string_temp = string_temp.replace('D20', '3')
    string_temp = string_temp.replace('D40', '4')
    string_temp = string_temp.replace('D43', '4')
    string_temp = string_temp.replace('D44', '4')
    string_list.append(string_temp)
    
with open('new_' + test_path, mode='w', newline='\n') as f:
    for string_row in string_list:
        f.write(string_row + '\n')