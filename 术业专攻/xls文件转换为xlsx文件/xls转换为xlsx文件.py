import os
import win32com.client as win32
from openpyxl import Workbook,load_workbook
path=r'D:\WORK\Python\Python code\术业专攻\xls文件转换为xlsx文件\转换前/'
new_path=r'D:\WORK\Python\Python code\术业专攻\xls文件转换为xlsx文件\转换后/'
files=os.listdir(path)
for file in files:
    fname = path+file
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(new_path+file+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    # wb.SaveAs(fname[:-1], FileFormat = 56)      #FileFormat = 56 is for .xls extension
    wb.Close()
    excel.Application.Quit()
