import csv
with open(r'D:\WORK\Python\Python code\第16关\test.csv','a',newline = '')  as f:
    writer=csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])
with open(r'D:\WORK\Python\Python code\第16关\test.csv',newline = '')  as f:
    result=csv.reader(f)
    for i in result:
        print(i)



        # ['4', '猫砂', '25', '1022', '886']、['5', '猫罐头', '18', '2234', '3121']