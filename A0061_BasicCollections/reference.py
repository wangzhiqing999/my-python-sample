# coding:utf-8

# 参考.


# 当你创建一个对象并给它赋一个变量的时候，这个变量仅仅 参考 那个对象，而不是表示这个对象本身！
# 也就是说，变量名指向你计算机中存储那个对象的内存。
# 这被称作名称到对象的绑定。



# 简单赋值这种情况， 与 C# 的处理机制一样。
print ('===== 步骤1：测试简单的赋值处理! =====');

# 初始化列表.
shoplist = ['apple', 'mango', 'carrot', 'banana']

# 简单赋值.
mylist = shoplist;

print ('shoplist 列表中的元素为：', shoplist);
print ('mylist 列表中的元素为：', mylist);


print ('删除 shoplist 列表中的数据!');
del shoplist[0];

print ('shoplist 列表中的元素为：', shoplist);
print ('mylist 列表中的元素为：', mylist);

print ('注意观察，简单的赋值处理，当一个列表删除一个数据以后，另外一个也少数据了。');




print ('\n===== 步骤2：测试拷贝的处理! =====');
mylist = shoplist[:];

print ('shoplist 列表中的元素为：', shoplist);
print ('mylist 列表中的元素为：', mylist);


print ('删除 shoplist 列表中的数据!');
del shoplist[0];

print ('shoplist 列表中的元素为：', shoplist);
print ('mylist 列表中的元素为：', mylist);

print ('注意观察，拷贝的处理，当一个列表删除一个数据以后，另外一个数据没有影响。');


