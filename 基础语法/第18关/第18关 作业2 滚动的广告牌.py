
# 运行前可将第8行改为 for i in range(20) 控制一下循环次数。
# 或者，可以直接运行，然后用“刷新网页”这种方法强行打断程序。
import os, time
def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
    content = ' 张君正你是个大笨蛋 '  # 广告词可自定义。
    for i in range(20):
        os.system('cls')  # 完成清屏：清屏和打印结合起来，形成滚动效果。
        print(content)
        content = content[1:] + content[0]  # 这行代码相当于：将字符串中第一个元素移到了最后一个。
        time.sleep(1)  # 你可以改下时间，体会“循环周期”和“滚动速度”之间的关联。
if __name__ == '__main__':  # 类里面学到的检测方法，在函数中其实也可以用。
    main()