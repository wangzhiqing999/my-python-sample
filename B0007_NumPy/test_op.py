import numpy as np



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("加法:", a + b)
print("减法:", a - b)
print("乘法:", a * b)
print("除法:", a / b)
print()



# 二维数组的运算.
# 矩阵乘法
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.dot(A, B)
print("矩阵乘法结果:\n", dot_product)

# 求逆矩阵
inv_A = np.linalg.inv(A)
print("矩阵 A 的逆矩阵:\n", inv_A)

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print("矩阵 A 的特征值:", eigenvalues)
print("矩阵 A 的特征向量:\n", eigenvectors)
print()





a = np.array([1, 2, 3, 4, 5])
print("数组的平均值:", np.mean(a))
print("数组的中位数:", np.median(a))
print("数组的标准差:", np.std(a))
print("数组的最大值:", np.max(a))
print("数组的最小值:", np.min(a))
print()



# 索引访问
print("数组的第一个元素:", a[0])

# 切片访问
print("数组的前三个元素:", a[0:3])
print()


arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("原始数组形状:", arr_2d.shape)

# 改变数组形状
reshaped_a = arr_2d.reshape(3, 2)
print("重塑后的数组形状:", reshaped_a.shape)

# 展平数组
# 使用 flatten() 方法将多维数组展平为一维数组。
flattened_arr = arr_2d.flatten()
print("展平后的数组:", flattened_arr)


# 数组转置
transposed_a = arr_2d.T
print("转置后的数组形状:", transposed_a.shape)


print("二维数组的第二行:", arr_2d[1])
print("二维数组的第一列:", arr_2d[:, 0])