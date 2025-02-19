# coding:utf-8

# 使用文件.


# 关于文件的帮助信息， 可以在 Python 命令行中输入：
# help(open)
 






# 准备用于写入文件的内容.
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!

测试中文汉字， 是否能正确地写入与读取！
'''


print("将文本信息，写入到文件中去...")

# open for 'w'riting   
# 以写入方式， 打开文件 poem.txt
f = open('poem.txt', 'w')

# 将前面的文本信息， 写入到文件当中去.
f.write(poem)

# 关闭文件.
f.close()



 
print("从文件中，读取文本信息...")

# if no mode is specified, 'r'ead mode is assumed by default
# 以读取方式， 打开文件. 
f = open('poem.txt')

# 开始循环处理.
while True:
    # 读取一行数据.
    line = f.readline()
    # 如果读取到结束了，那么跳出循环.
    if len(line) == 0: # Zero length indicates EOF
        break
    # 调试
    print (line)

# 关闭文件.
f.close()