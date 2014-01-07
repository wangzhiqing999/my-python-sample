# coding:utf-8

# for 的测试.


# Python 中的 for，  与 C/C++ 中的 for(int i=1; i < 5; i++) 不同.
# Python 中的 for，  相当于 C# 中的 foreach(int i in new int[]{1,2,3,4})

# 这里的 range返回一个序列的数。
# 这个序列从第一个数开始到第二个数为止。
# 例如，range(1,5)给出序列[1, 2, 3, 4]。
# 默认地，range的步长为1。
# 如果我们为range提供第三个数，那么它将成为步长。
# 例如，range(1,5,2)给出[1,3]。
# 记住，range 向上 延伸到第二个数，即它不包含第二个数。
for i in range(1, 5):
    print ("for 循环执行过程中！", i);
else:
    # else部分是可选的。如果包含else，它总是在for循环结束后执行一次，除非遇到break语句。
    print ('for 循环执行结束！');


print ("测试 for 循环中的 continue 与 break.");

for i in range(1, 8):
    if (i == 3):
        print ("for 循环中使用 continue 语句！");
        continue;
    print ("for 循环执行过程中！", i);
    if (i == 6):
        print ("for 循环中使用 break 语句！");
        break;
else:
    # else部分是可选的。如果包含else，它总是在for循环结束后执行一次，除非遇到break语句。
    print ('for 循环执行结束！');

