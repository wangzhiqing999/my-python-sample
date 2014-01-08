# coding:utf-8

# 列表综合

# 通过列表综合，可以从一个已有的列表导出一个新的列表。
# 例如，你有一个数的列表，而你想要得到一个对应的列表，使其中所有大于2的数都是原来的2倍。对于这种应用，列表综合是最理想的方法。


# 初始列表.
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
];
print ("初始列表：", matrix);


# 列表综合
newmatrix = [[row[i] for row in matrix] for i in range(4)]
print ("新列表：", newmatrix);

