# coding:utf-8

# if 的测试.


number = 23;

# 注意：python3.x系列不再有 raw_input 函数。3.x中 input 和从前的 raw_input 等效
guess = int(input('请输入一个整数: '));


if (guess == number):
    # Python 中，不像 类C语言的那种， 有 {  }  来表示 if() {多行代码}  else {多行代码}
    # 是靠代码前的空格来判断的。
    # New block starts here
    print ('数据匹配！');
    print ("if 情况下的第二行代码！");
    # New block ends here
elif (guess < number):
    # Another block
    print ('您输入的数字太小了！')
    # You can do whatever you want in a block ...
else:
    print ('您输入的数字太大了！')
    # you must have guess > number to reach here


# 当代码回到顶格， 前面没有空格的情况下.
# 那么这里认为是 前面的 if 的代码结束了. 是新的代码段了.
print ('代码处理结束！！！');