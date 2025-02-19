import pandas as pd

# 创建一个包含分组信息的 DataFrame
data ={'Name':['Alice','Bob','Charlie','Alice'],'Age':[25,30,35,40],'Salary':[50000,60000,70000,80000]}
df = pd.DataFrame(data)
print(df)



# 按 Name 分组并计算每组的平均年龄和平均薪资
print('--- mean ---')
print(df.groupby('Name').agg({'Age':'mean','Salary':'mean'}))


print('--- min ---')
print(df.groupby('Name').agg({'Age':'min','Salary':'min'}))


print('--- max ---')
print(df.groupby('Name').agg({'Age':'max','Salary':'max'}))


print('--- sum ---')
print(df.groupby('Name')['Salary'].sum())