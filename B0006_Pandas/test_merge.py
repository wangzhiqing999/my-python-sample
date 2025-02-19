import pandas as pd


# 创建两个 DataFrame
df1 = pd.DataFrame({'Name':['Alice','Bob'],'Age':[25,30]})
df2 = pd.DataFrame({'Name':['Alice','Bob'],'Salary':[50000,60000]})


print(df1)
print(df2)


# 使用 merge 合并
df_merge = pd.merge(df1, df2, on='Name')
print(df_merge)