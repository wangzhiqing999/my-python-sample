# coding:utf-8

# 数组.
# 可以通过 help(tuple) 获得完整的知识。



# 数组的初始化方式.   (数组的元素)
zoo = ('wolf', 'elephant', 'penguin', 'wolf',);
# len 函数， 用于获取 列表的长度.
print ('数组长度 len(zoo) = ', len(zoo));
print ("数组长度 zoo.count('wolf') = ", zoo.count("wolf"));




# 初始化一个新的数组. (最后一个元素， 是一个数组)
new_zoo = ('monkey', 'dolphin', zoo);
print ('新数组长度 len(new_zoo) = ', len(new_zoo));

print ('新数组中的元素为：', new_zoo);
print ('新数组中的第3个元素 new_zoo[2] 为：', new_zoo[2]);
print ('新数组中的第3个元素的第3个元素 new_zoo[2][2] 为：', new_zoo[2][2]);





print ("测试  数组与打印语句！");
age = 22
name = 'Swaroop'
print ('%s is %d years old' % (name, age) );
print ('Why is %s playing with that python?' % name);
