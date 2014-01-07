# coding:utf-8

# 序列.



# 首先， 初始化一个列表.
shoplist = ['apple', 'mango', 'carrot', 'banana']

print ('当前列表中的元素为：', shoplist);



# Indexing or 'Subscription' operation
print ('列表中的第 0 个元素', shoplist[0]);
print ('列表中的第 1 个元素', shoplist[1] );
print ('列表中的第 2 个元素', shoplist[2] );
print ('列表中的第 3 个元素', shoplist[3] );

print ('列表中的第 -1 个元素 （意味着从后面向前，第1个元素）', shoplist[-1] );
print ('列表中的第 -2 个元素 （意味着从后面向前，第2个元素）', shoplist[-2] );


# Slicing on a list
print ('列表中的第1个（含） 到第3个（不含） 元素：', shoplist[1:3] );
print ('列表中的第2个（含） 到底：', shoplist[2:] );
print ('列表中的第1个（含） 到从后面向前第1个（不含） 元素', shoplist[1:-1] );
print ('列表中的全部元素：', shoplist[:] );





# Slicing on a string
name = 'swaroop'

print ('当前的字符串为：', name);


print ( '字符串中，从第1个（含）到第3个（不含）字符：', name[1:3] );
print ( '字符串中，从第2个（含）到底：', name[2:] );
print ( '字符串中，从第1个（含）到第从后面向前第1个（不含）字符：', name[1:-1] );
print ( '字符串中，全部的字符：', name[:] );


