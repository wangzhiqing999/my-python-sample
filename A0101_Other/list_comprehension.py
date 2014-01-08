# coding:utf-8

# 列表综合

# 通过列表综合，可以从一个已有的列表导出一个新的列表。
# 例如，你有一个数的列表，而你想要得到一个对应的列表，使其中所有大于2的数都是原来的2倍。对于这种应用，列表综合是最理想的方法。


# 初始列表.
listone = [1, 2, 3, 4, 5, 4, 3, 2, 1];
print ("初始列表：", listone);


# 列表综合
# 这里相当于  select 2*i from listone where i>2 的处理.
listtwo = [2*i for i in listone if i > 2];
print ("新列表：", listtwo);

