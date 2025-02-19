import numpy as np


def print_array(array):
    print('--------------------------------')
    print("数组形状:", array.shape)  # 数组的维度
    print("数组维度:", array.ndim)  # 数组的维数
    print("数组元素个数:", array.size)  # 数组中元素的总数
    print("数组元素类型:", array.dtype)  # 数组元素的数据类型
    print(f"数组元素:\n{array}")



# 创建一个简单的NumPy数组
arr = np.array([1, 2, 3, 4, 5])
print_array(arr)

# 数组操作
print("数组求和:", np.sum(arr))
print("数组平均值:", np.mean(arr))
print("数组最大值:", np.max(arr))




# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print_array(arr2)

# 数组操作
print("数组求和:", np.sum(arr2))
print("数组平均值:", np.mean(arr2))
print("数组最大值:", np.max(arr2))




# 创建全零数组
zeros_array = np.zeros((2, 3))  # 2 行 3 列
print_array(zeros_array)


# 创建全一数组
ones_array = np.ones((3, 2))  # 3 行 2 列
print_array(ones_array)


# 创建指定值的数组
full_array = np.full((2, 2), 7)  # 2 行 2 列，值都为 7
print_array(full_array)


# 创建等差数列
array1 = np.arange(0, 10, 2)  # 从 0 到 10，步长为 2
print_array(array1)


# 创建等比数列
array2 = np.linspace(0, 1, 5)  # 从 0 到 1，均匀分成 5 个点
print_array(array2)
