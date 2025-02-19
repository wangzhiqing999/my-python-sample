import pandas as pd

# 创建多层索引
index = pd.MultiIndex.from_tuples([('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'C')], names=['Name','Group'])
data = {'Age': [25, 30, 35]}
df = pd.DataFrame(data, index=index)
print(df)

# 计算每组的平均年龄
print(df.groupby('Group').mean())