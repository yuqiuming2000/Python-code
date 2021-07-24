movie = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}
name = input('你想查询哪个演员？')
for i in movie:
    actors = movie[i]
    #取出字典的值
    if name in actors:
        print(name+'出演了电影'+i)
