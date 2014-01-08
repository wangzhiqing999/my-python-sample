# coding:utf-8

# 使用sys模块.



# 利用import语句 输入 sys模块。
# 基本上，这句语句告诉Python，我们想要使用这个模块。
# sys模块包含了与Python解释器和它的环境有关的函数。

# 如果需要了解详细的 sys 模块的信息
# 可以在 Python 控制台上执行
# import sys
# help(sys)


import sys




print("主机操作系统：", sys.platform);
print("Python 版本：", sys.version);
print("控制台输出编码：", sys.stdout.encoding);
print("默认编码：", sys.getdefaultencoding());
print ('命令行参数为:');

# sys模块中的argv变量通过使用点号指明——sys.argv——
# 这种方法的一个优势是这个名称不会与任何在你的程序中使用的argv变量冲突。
# 另外，它也清晰地表明了这个名称是sys模块的一部分。
for i in sys.argv:
    print (i);

print ('\n\nThe PYTHONPATH is', sys.path, '\n');




# 运行时， python using_sys.py 1 2 3 4 5  来查看执行的效果.
