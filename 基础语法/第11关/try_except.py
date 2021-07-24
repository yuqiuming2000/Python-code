while True:
    try:
        age = int(input('你今年几岁了？'))
        break
    except ValueError:
        print('你输入的不是数字！')
