# -*- coding: utf-8 -*-


# 使用 list 实现堆栈的效果（后进先出）




stack = [1, 2, 3, 4, 5];
print("初始化！", stack);

stack.append(6);
print("入一个数据后！", stack);

stack.append(7);
print("入一个数据后！", stack);


print("出一个数据", stack.pop(), "之后", stack);
print("出一个数据", stack.pop(), "之后", stack);
print("出一个数据", stack.pop(), "之后", stack);
print("出一个数据", stack.pop(), "之后", stack);
