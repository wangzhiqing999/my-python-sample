# 数据清洗：如何处理缺失值、异常值？是否需要填充或删除？

详细解答：
## 处理缺失值：

### 删除行：
如果缺失值较少，可以直接删除包含缺失值的行。
```
df.dropna(inplace=True)
```

### 删除列：
如果某列缺失值较多，可以考虑删除该列。
```
df.drop(columns=['ColumnName'], inplace=True)
```

### 均值填充：
适用于数值型数据，用列的均值填充缺失值。
```
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

### 中位数填充：
适用于数值型数据，用列的中位数填充缺失值。
```
df['Age'].fillna(df['Age'].median(), inplace=True)
```

### 众数填充：
适用于分类数据，用列的众数填充缺失值。
```
df['Name'].fillna(df['Name'].mode()[0], inplace=True)
```

### 前向/后向填充：
用前一个或后一个非缺失值填充。
```
df['Age'].fillna(method='ffill', inplace=True)  # 前向填充
df['Age'].fillna(method='bfill', inplace=True)  # 后向填充
```

### 填充缺失值：

### 删除缺失值：


## 处理异常值：
### 删除异常值：
直接删除检测到的异常值。
```
df.drop(index, inplace=True)
```

### 修正异常值：
用均值、中位数或众数替换异常值。
```
df.loc[index, 'Age'] = df['Age'].mean()
```

### 标准差法：
假设数据服从正态分布，超出均值±3倍标准差的值视为异常值。
```
mean = df['Age'].mean()
std = df['Age'].std()
df = df[(df['Age'] >= mean - 3 * std) & (df['Age'] <= mean + 3 * std)]
```

### 四分位数法：
使用四分位数范围（IQR）检测异常值。
```
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Age'] >= Q1 - 1.5 * IQR) & (df['Age'] <= Q3 + 1.5 * IQR)]
```





