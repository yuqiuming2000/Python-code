import os
from docx import Document
from docxcompose.composer import Composer
from docx import Document as Document_compose
result=[]
def search(path=".", name=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            search(item_path, name)
        elif os.path.isfile(item_path):
            if name in item:
                global result
                result.append(item_path)
                print (item_path)

search(path="术业专攻\收购验收资料\申请报告汇总\转换后docx文件夹", name=".docx")
print(result)
# 合并文档的列表


files = result
def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(1, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save("术业专攻\收购验收资料\申请报告汇总\汇总后/汇总后.docx")
combine_all_docx(result[0],result)