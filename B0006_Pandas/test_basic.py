import pandas as pd



# 创建一个简单的 DataFrame
data = {'Name':['ZhangSan', 'Alice', 'Bob', 'Charlie', None], 'Age':[33,25,30,35,64]}

print('-----初始化-----')
df = pd.DataFrame(data)
print(df)


print('-----删除空值-----')
df.dropna(inplace=True)
print(df)


print('-----设置索引-----')
df.set_index('Name', inplace=True)
print(df)
