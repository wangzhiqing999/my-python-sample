# -*- coding: utf-8 -*-


# 使用 list 实现队列的效果（先进先出）


from collections import deque


queue = deque([1, 2, 3, 4, 5]);
print("初始化！", queue);

queue.append(6);
print("入一个数据后！", queue);

queue.append(7);
print("入一个数据后！", queue);


print("出一个数据", queue.popleft(), "之后", queue);
print("出一个数据", queue.popleft(), "之后", queue);
print("出一个数据", queue.popleft(), "之后", queue);
print("出一个数据", queue.popleft(), "之后", queue);
