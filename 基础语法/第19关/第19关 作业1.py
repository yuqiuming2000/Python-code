# 结构一：导入模块，涉及知识点：【模块】
import requests
import json
import random
import time
# 结构二：导入选择题，涉及知识点：【文件读取】、【异常处理】
try:
    with open('./new_year_questions.json', encoding='utf-8') as file:
        questions_json = json.loads(file.read())
except FileNotFoundError:
    res = requests.get('https://static.pandateacher.com/new_year_questions.json')
    with open('./new_year_questions.json', 'w', encoding='utf-8') as file:
        file.write(res.text)
    questions_json = res.json()
except Exception as e:
    print("加载题目失败，失败原因：{}".format(e))
    exit()
questions_list = questions_json['questions_list']
result = questions_json['result']
# 结构三：设置计分器，涉及知识点：【字典】
point = {
    1: 0,
    2: 0,
}
question=random.choice(result)
answer=input(question)