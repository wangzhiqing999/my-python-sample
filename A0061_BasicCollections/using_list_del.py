# -*- coding: utf-8 -*-


# list 中，使用 del 的处理.


a = [-1, 1, 66.25, 333, 333, 1234.5];\
print("初始化！", a);


del a[0];
print("del a[0] 之后", a);


del a[2:4];
print("del a[2:4] 之后", a);


del a[:];
print("del a[:] 之后", a);
