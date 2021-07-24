import csv
# with open('./第三关作业.csv','r',newline='')as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
with open('./第三关作业.csv', 'r', newline='') as csv_file:
    # 将文件对象转换为DictReader对象
    csv_reader = csv.DictReader(csv_file)
    # 获取表头
    headers = csv_reader.fieldnames
    # 打印表头
    print('表头：{}'.format(headers))
    # 遍历DictReader对象
    for csv_row in csv_reader:
        # 打印数据
        print(csv_row)