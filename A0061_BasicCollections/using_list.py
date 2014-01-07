# coding:utf-8

# 列表.
# 可以通过 help(list) 获得完整的知识。


# 列表的初始化方式.   [列表的元素] 
shoplist = ['apple', 'mango', 'carrot', 'banana', 'apple' ];

# len 函数， 用于获取 列表的长度.
print ('列表长度 len(list) = ', len(shoplist));
print ("列表长度 list.count('apple') = ", shoplist.count("apple"));

print ('列表中的元素：');
for item in shoplist:
    print (item);


print ('向列表尾部中追加一个元素  rice');
# 列表.append() 方法，用于向列表中追加元素.
shoplist.append('rice');
print ('当前列表中的元素为：', shoplist);


print ('向列表中间插入一个元素  ABC');
# 列表.insert() 方法，用于向列表中插入追加元素.
shoplist.insert(2, 'ABC');
print ('当前列表中的元素为：', shoplist);



print ('对列表进行排序的处理！');
# 列表.sort() 方法，对列表中的数据进行排序.
shoplist.sort()
print ('当前列表中的元素为：', shoplist);


print ('对列表进行转置的处理！');
# 列表.reverse() 方法，对列表中的数据进行转置.
shoplist.reverse()
print ('当前列表中的元素为：', shoplist);




print ('列表中的第一个元素是：', shoplist[0]);
olditem = shoplist[0];
print ('尝试 del list[0] 删除列表中的第一个元素', shoplist[0]);
# del 用于删除 列表中的元素.
del shoplist[0];
print ('当前列表中的元素为：', shoplist);



print ('尝试 shoplist.remove(shoplist[3]) 删除列表中的元素');
# list.remove(list[0]) 用于删除 列表中的元素.
shoplist.remove(shoplist[3]);
print ('当前列表中的元素为：', shoplist);



print ('尝试使用 pop 函数，返回并删除列表中的最后一个元素');
# pop 函数，用于 移除并返回最后一个元素.
olditem = shoplist.pop();
print ('当前列表中的元素为：', shoplist);
print ('pop函数返回的结果为：', olditem);



print ('尝试清除列表中的所有元素');
# clear() 用于删除 列表中的所有元素.
shoplist.clear();
print ('当前列表中的元素为：', shoplist);

