# coding:utf-8

# try..finally 处理.



import time

try:
    # 读取文件.
    f = open('finally.py',  encoding="utf-8");
    
    while True: # our usual file-reading
        # 一行一行读取.
        line = f.readline()
        # 读取到结束的时候，跳出循环.
        if len(line) == 0:
            break
        # 休眠2秒.
        time.sleep(2)
        # 输出文件行内容.
        print (line.encode("utf-8"));
finally:
    # 关闭文件.
    f.close()
    print ('处理完毕，关闭已打开的文件.');



