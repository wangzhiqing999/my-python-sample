# -*- coding: utf-8 -*-

# __annotations__  效果上面可以这么用.


def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("Annotations:", f.__annotations__)
    ann = f.__annotations__
    print("ham=", ann["ham"])
    print("eggs=", ann["eggs"])
    print("return=", ann["return"])

    print("Arguments:", ham, eggs)


f('wonderful')

f(1024, 'wonderful')
