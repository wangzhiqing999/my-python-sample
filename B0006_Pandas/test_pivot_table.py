import pandas as pd


# ----- 按列进行分组汇总 -----
# 示例数据
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 250, 130]
}
df = pd.DataFrame(data)

# 按 'Category' 分组汇总 'Sales'，计算总和
pivot_table = pd.pivot_table(df, index='Category', values='Sales', aggfunc='sum')
print(pivot_table)
print()



# ----- 边际总计（margins） -----
# 在透视表中添加边际总计
pivot_table = pd.pivot_table(df, index='Category', values='Sales', aggfunc='sum', margins=True)
print(pivot_table)
print()



# ----- 多列分组汇总 -----
# 扩展示例数据，增加地区信息
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Sales': [100, 200, 150, 250, 130]
}
df = pd.DataFrame(data)

# 按 'Category' 和 'Region' 进行多列分组汇总 Sales 的总和
pivot_table = pd.pivot_table(df, index=['Category', 'Region'], values='Sales', aggfunc='sum')
print(pivot_table)
print()


# ----- 列字段的聚合 -----
# 按 'Region' 在行方向，'Category' 在列方向进行分组，汇总 'Sales'
pivot_table = pd.pivot_table(df, index='Region', columns='Category', values='Sales', aggfunc='sum')
print(pivot_table)
print()



# ----- 处理缺失值 -----
# 将透视表中的缺失值（NaN）填充为 0
pivot_table = pd.pivot_table(df, index='Region', columns='Category', values='Sales', aggfunc='sum', fill_value=0)
print(pivot_table)
print()



# ----- 指定多种聚合函数 -----
# 对 Sales 列应用多个聚合函数：求和，总数和平均值
pivot_table = pd.pivot_table(df, index='Category', values='Sales', aggfunc=['sum', 'mean', 'count'])
print(pivot_table)
print()



# ----- 多列聚合 -----
# 示例数据，增加多个数值列
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 250, 130],
    'Profit': [30, 50, 40, 70, 20]
}
df = pd.DataFrame(data)

# 对 Sales 和 Profit 列分别进行求和
pivot_table = pd.pivot_table(df, index='Category', values=['Sales', 'Profit'], aggfunc='sum')
print(pivot_table)
print()


# ----- 分层索引（多级索引） -----
# 示例数据
data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Region': ['North', 'South', 'North', 'South', 'North'],
    'Sales': [100, 200, 150, 250, 130],
    'Profit': [30, 50, 40, 70, 20]
}
df = pd.DataFrame(data)

# 生成多级索引的透视表
pivot_table = pd.pivot_table(df, index=['Category', 'Region'], values=['Sales', 'Profit'], aggfunc='sum')
print(pivot_table)
print()
