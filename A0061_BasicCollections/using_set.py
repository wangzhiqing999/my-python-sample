# -*- coding: utf-8 -*-


# Set 的使用.
# list  使用 [] 包含多个元素.
# tuple 使用 () 包含多个元素.
# Set   使用  {} 包含多个元素.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'};
print("初始数据",  basket);

print("'orange' in basket =", 'orange' in basket );
print("'crabgrass' in basket =", 'crabgrass' in basket );




a = set('abracadabra')
b = set('alacazam')

print("初始数据a=",  a);
print("初始数据b=",  b);

# a-b 相当于返回  从a里面排除掉  a与b 都有的元素
print("a-b=",  (a-b));

# a|b 相当于返回全部的唯一的数据.
print("a|b=",  (a|b));

# a&b 相当于返回 a 与 b 都有的数据.
print("a&b=",  (a&b));

# a^b 相当于返回 全部里面， 排除掉那些 a 与 b 都有的数据.
print("a^b=",  (a^b));

