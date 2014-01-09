# -*- coding: utf-8 -*-

# 使用 json 来进行 序列化与反序列化的处理.


import json 


# 用于存储数据的文件.
shoplistfile = 'shoplist.json';

# 定义变量.
shoplist = ['apple', 'mango', 'carrot', '测试中文汉字'];
print ("内存中的数据列表", shoplist);



print ("数据写入到 json 文件中");

# 这里打开文件.
with open(shoplistfile, 'w', encoding='utf-8') as f:
    # 将内存中的对象， 序列化到文件当中.
    json.dump(shoplist, f);

# 关闭文件.
f.close();

# 释放内存空间.
del shoplist # remove the shoplist




print ("从 json 文件中加载数据.");

# 打开文件
with open(shoplistfile, "r", encoding='utf-8') as f:
    storedlist = json.load(f);
    print ("从json文件中读取出来的数据列表", storedlist);
# 关闭文件.
f.close();
