import numpy as np



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("加法:", a + b)
print("减法:", a - b)
print("乘法:", a * b)
print("除法:", a / b)
print()




a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("矩阵乘法:", np.dot(a, b))
print()



a = np.array([1, 2, 3, 4, 5])
print("数组的平均值:", np.mean(a))
print("数组的中位数:", np.median(a))
print("数组的标准差:", np.std(a))
print("数组的最大值:", np.max(a))
print("数组的最小值:", np.min(a))
print()



a = np.array([[1, 2, 3], [4, 5, 6]])
print("原始数组形状:", a.shape)

# 改变数组形状
reshaped_a = a.reshape(3, 2)
print("重塑后的数组形状:", reshaped_a.shape)

# 数组转置
transposed_a = a.T
print("转置后的数组形状:", transposed_a.shape)