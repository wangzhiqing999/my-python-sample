# coding:utf-8

# 储存器.




# Python提供一个标准的模块，称为pickle。
# 使用它你可以在一个文件中储存任何Python对象，
# 之后你又可以把它完整无缺地取出来。这被称为 持久地 储存对象。
# 你可以使用它们中的任一个，而我们在这里将使用cPickle模块。记住，我们把这两个模块都简称为pickle模块。
#
# 具体细节操作， 可以在 Python 命令行中输入：
# import pickle
# help(pickle)



import pickle as p


# 用于存储数据的文件.
shop_list_file = 'shop_list.data'

# 定义变量.
shop_list = ['apple', 'mango', 'carrot', '测试中文汉字']
print ("内存中的数据列表", shop_list)

print ("数据写入到文件中")

# 注意：这里打开文件的时候， 需要使用  wb  的参数。而不是简单的  w 
f = open(shop_list_file, 'wb')

# 将内存中的对象， 序列化到文件当中.
p.dump(shop_list, f)  # dump the object to a file
# 关闭文件.
f.close()

# 释放内存空间.
del shop_list # remove the shop_list




print ("从文件中加载数据.")

# 注意：这里打开文件的时候， 需要使用  rb  的参数。而不是忽略掉， 使用默认的 rt
f = open(shop_list_file, "rb")

shop_list = p.load(f)
print ("从文件中读取出来的数据列表", shop_list)
# 关闭文件.
f.close()
