
import os
import time
import win32com
from win32com.client import Dispatch
 
def doc_to_docx(path):
   w = win32com.client.Dispatch('Word.Application')
   w.Visible = 0
   w.DisplayAlerts = 0
   doc = w.Documents.Open(path)
   # 这里必须要绝对地址,保持和doc路径一致
   new_file_path=new_path+file+'.docx'
   time.sleep(3) # 暂停3s，否则会出现-2147352567,错误
   doc.SaveAs(new_file_path,12,False,"",True,"",False,False,False,False)
   # doc.Close() 开启则会删掉原来的doc
   w.Quit()# 退出
   return new_file_path
path=r'D:\WORK\Python\Python code\术业专攻\收购验收资料\申请报告汇总\调整前/'
new_path=r'D:\WORK\Python\Python code\术业专攻\收购验收资料\申请报告汇总\调整后/'

files=os.listdir(path)
for file in files:
    file=file[:2]
    print(file)
    file_path=path+file
    # new_file_path=new_path+'file.docx'
    doc_to_docx(file_path)