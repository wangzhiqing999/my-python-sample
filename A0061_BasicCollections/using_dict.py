# coding:utf-8

# 数组.
# 可以通过 help(dict) 获得完整的知识。


# 初始化 字典.

ab = {  '张三' : 'zhang3@test.info',
        '李四' : 'li4@wall.org',
        '王五' : 'wang5@ruby-lang.org',
        '赵六' : 'zhao6@hotmail.com'
     };

# len 函数， 用于获取 字典的长度.
print ('字典长度 len(ab) = ', len(ab));

print ('当前字典中的元素为：', ab);

print ("张三 的电子邮件地址是 %s" % ab['张三']);


print("向地址簿里面增加一个 key/value ");
# Adding a key/value pair
ab['田七'] = 'tian7@python.org'
print ('当前字典中的元素为：', ab);


# Deleting a key/value pair
print("从地址簿里面删除一个 key/value ");
del ab['张三']
print ('当前字典中的元素为：', ab);



print("for 语句， 遍历每一个 key/value ");
for name, address in ab.items():
    print ('Contact %s at %s' % (name, address) );

print("in 语句， 判断 key 是否存在 ");
if '李四' in ab:
    print ("李四的电子邮件是 %s" % ab['李四']);
    
