# -*- coding: utf-8 -*-

# 使用 json 来进行 序列化与反序列化的处理.


import json 


# 用于存储数据的文件.
shop_list_file = 'shop_list.json'

# 定义变量.
shop_list = ['apple', 'mango', 'carrot', '测试中文汉字']
print ("内存中的数据列表", shop_list)



print ("数据写入到 json 文件中")

# 这里打开文件.
with open(shop_list_file, 'w', encoding='utf-8') as f:
    # 将内存中的对象， 序列化到文件当中.
    json.dump(shop_list, f)

# 关闭文件.
f.close()

# 释放内存空间.
del shop_list # remove the shop_list




print ("从 json 文件中加载数据.")

# 打开文件
with open(shop_list_file, "r", encoding='utf-8') as f:
    stored_list = json.load(f)
    print ("从json文件中读取出来的数据列表", stored_list)
# 关闭文件.
f.close()
