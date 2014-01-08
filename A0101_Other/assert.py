# coding:utf-8

# assert语句

# assert语句用来声明某个条件是真的。
# 例如，如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，
# 那么assert语句是应用在这种情形下的理想语句。
# 当assert语句失败的时候，会引发一个AssertionError。




# 初始化.
mylist = ['item'];

# 首次断言.(成功)
assert len(mylist) >= 1;

print(mylist.pop());

# 再次断言.(失败)
assert len(mylist) >= 1;