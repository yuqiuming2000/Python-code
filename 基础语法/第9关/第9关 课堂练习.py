#定义一个带有两个参数的函数，函数的功能是返回两个参数中较大的那个值；二、调用函数，将99的平方和8888赋值给参数，并将较大值打印出来
def bigger(a,b):
    if a>=b:
        return a
    else:
        return b
print(bigger(99**2,8888))
