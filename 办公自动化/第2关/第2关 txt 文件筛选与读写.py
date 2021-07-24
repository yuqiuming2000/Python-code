
import os
path='./'
filenames=os.listdir(path)
print(filenames)
keyword=input('请输入您要查找的关键词：')  
for i in filenames:
    if '.txt' in i:
        # print(i)
        target_file = path + i
        # print(target_file)
        with open(target_file, 'r', encoding='utf-8') as file:
            content = file.read()
            # print(content)
            if keyword in content:
                print('终于找到了，文件{}包含了关键词{}'.format(target_file,keyword))






