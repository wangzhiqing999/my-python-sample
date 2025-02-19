import pandas as pd

# 创建两个 DataFrame
df1 = pd.DataFrame({'Name':['Alice','Bob'],'Age':[25,30]})
df2 = pd.DataFrame({'Name':['Charlie','David'],'Age':[35,40]})


print(df1)
print(df2)

# 使用 concat 合并
df_concat = pd.concat([df1, df2])
print(df_concat)