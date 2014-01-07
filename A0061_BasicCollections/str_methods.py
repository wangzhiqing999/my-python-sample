# coding:utf-8

# 字符串的方法.
# 更多细节信息， 可通过  help(str) 进行查询.


# 定义一个字符串对象.
name = 'hello world PYTHON hello world PYTHON';
age = '16';
abc = "cdfgxyz";


print ("初始字符 = ", name);

# capitalize
print ("capitalize 函数用于 首字母大写，其他小写！" , name.capitalize() );


# casefold
print ("casefold 函数用于 全部字母小写！", name.casefold() );

# lower
print ("lower 函数用于 全部字母小写！", name.lower() );

# upper
print ("upper 函数用于 全部字母大写！", name.upper() );

# title 
print( "title 函数用于将字符串中的每一个单词，设置成首字母大写：", name.title());



# startswith
print ("startswith 函数用于判断， 字符串是否是 指定参数开头的！", name.startswith('hello'),  name.startswith('world') );

# endswith
print ("endswith 函数用于判断， 字符串是否是 指定参数结尾的！", name.endswith('PYTHON'),  name.endswith('python') );

# find
print( "find 函数用于查询 参数在当前字符串中的位置:", name.find('world'), name.find('Xyz'));

# isalnum
print( "isalnum 函数用于返回数据是否是按照数字次序:", name.isalnum(), age.isalnum());

# isalpha
print( "isalpha 函数用于返回数据是否是照字母次序的:", name.isalpha(), age.isalpha(), abc.isalpha());

# isdecimal
print( "isdecimal 函数用于返回数据是否是数字:", name.isdecimal(), age.isdecimal());

# isdigit
print( "isdigit 函数用于返回数据是否是数字:", name.isdigit(), age.isdigit());

# islower
print( "islower 函数用于返回数据是否是小写字母:", name.islower(), age.islower(), abc.islower());

# isupper
print( "isupper 函数用于返回数据是否是大写字母:", name.isupper(), age.isupper(), abc.isupper());



# isnumeric
print( "isnumeric 函数用于返回数据是否是数字:", name.isnumeric(), age.isnumeric());

# isprintable
print( "isprintable 函数用于返回数据是否是可打印的字符:", name.isprintable(), age.isprintable());

# isspace
print( "isspace 函数用于返回数据是否是空格:", name.isspace(), age.isspace());


# join 
mylist = ['Brazil', 'Russia', 'India', 'China']
print( "join 函数用于将一个列表，连接为字符串：", age.join(mylist), abc.join(mylist) );

# split 
print( "split 函数用于拆分一个字符串：", name.split(" "));


# replace
print( "replace 函数用于字符串替换:", name.replace(" ", "-"));


