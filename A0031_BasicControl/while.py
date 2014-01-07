# coding:utf-8

# while 的测试.


number = 23
running = True



# Python 中，不像 类C语言的那种， 有 {  }  来表示 while() {多行代码}
# 是靠代码前的空格来判断的。
while running:

    # 从控制台接收一个输入的数据.
    guess = int(input('请输入一个整数 : '));

    if guess == number:
        print ('数据匹配！');
        # 下面的语句， 设置标志位，结束循环处理.
        running = False;
    elif guess < number:
        print ('您输入的数字太小了！');
    else:
        print ('您输入的数字太大了！');

else:
    # 注意：与其他语言不同的地方是， Python 中的 while 循环中使用一个else从句。
    # 虽然看上去是多余的  “因为跟在while语句之后，这样可以取得相同的效果。”
    print ('循环执行结束！'); 
    # Do anything else you want to do here


print ('程序执行完毕！');