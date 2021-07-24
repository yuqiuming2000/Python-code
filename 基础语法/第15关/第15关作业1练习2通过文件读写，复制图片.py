with open(r'c:\Users\喻秋明\Desktop\test\test.jpg','rb') as file:
    data=file.read()
    with open(r'c:\Users\喻秋明\Desktop\test\copy.jpg','wb')as newfile:
        newfile.write(data)