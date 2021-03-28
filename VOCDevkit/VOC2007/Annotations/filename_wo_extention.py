import os

data_list = os.listdir('./images')  

print(data_list)

with open('test.txt', 'w') as f:
    for data in data_list:
        f.write(str(os.path.splitext(data)[0])+'\n')
