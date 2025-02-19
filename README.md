Python 学习的例子.
（以下例子运行于 python 3.3）


### A0001_HelloWorld
仅仅是一个 HelloWorld.



### A0011_BasicObject
基本的变量定义的方式.



### A0021_BasicOperator
基本的运算符.



### A0031_BasicControl
基本的控制结构.
包含
if.py               if / else 的处理。
while.py            while 循环的处理。
for.py              for 循环的处理。 ( continue 与 break 的例子在这里)


### A0041_BasicFunction
基本的函数的知识.
包含
func_def.py         函数的基本定义。
func_param.py       函数的参数。(包含固定参数，与可变参数的例子)
func_local.py       局部变量。
func_global.py      全局变量。
func_default.py     函数的参数的默认值。
func_key.py         使用关键参数。
func_return.py      函数的返回值。
func_doc.py         函数的文档。
func_annotations.py 函数的annotation


### A0051_BasicModule
基本的模块的知识.
包含
using_sys.py        使用 sys 模块的例子.
using_name.py       模块的名称（主程序）
using_name2.py      模块的名称（被其他程序引用）
mymodule.py         自定义模块的例子
mymodule_demo.py    调用自定义模块的例子.
mymodule_demo2.py   调用自定义模块的例子. (这里使用了 from..import语句 )



### A0061_BasicCollections
基本的集合处理.
包含
using_list.py           list 的使用. (列表)
using_list_del.py       list 中，使用 del 的处理.
using_list_as_stack.py  使用 list 实现堆栈的效果（后进先出）
using_list_as_queue.py  使用 list 实现队列的效果（先进先出）
using_tuple.py          tuple 的使用. (数组)
using_dict.py           dict  的使用. (字典)
using_set.py            set   的使用.
seq.py                  序列的处理.
reference.py            参考的情况. ( 也就是简单的赋值 与 拷贝的对比 )
str_methods.py          字符串的相关方法.




### A0071_BasicOO
基本的面向对象的处理.
包含
simplestclass.py    一个空白的类.
method.py           类里面定义方法.
class_init.py       __init__方法
objvar.py           类与对象的变量
inherit.py          继承





### A0081_BasicIO
输入/输出
包含
test_os.py			与操作系统进行交互的功能.
using_file.py       文件访问的处理.
using_file_with.py  访问文件的时候， 使用 with ， 来增加代码的可读性，以及避免误操作。
pickling.py         储存器 (用于序列化与反序列化)
using_json.py       使用 json 格式， 来进行序列化与反序列化。




### A0091_BasicException
异常的处理.
包含
try_except.py       try..except 处理异常.
raising.py          使用raise语句 引发 异常.
finally.py          try..finally




### A0101_Other
其他的内容.
包含
assert.py                       断言处理.
exec_eval.py                    exec和eval语句
lambda.py                       lambda形式
list_comprehension.py           列表综合
nested_list_comprehension.py    2维列表综合
repr.py                         repr函数



### A0111_Files

获取指定目录下，所有文件的名称与文件大小信息。






### B0001_mysql
将一个大的 sql 文件，拆分为多个小的 sql 文件。
依次执行多个小的 sql 文件。



一个目录下，有很多的 sql 文件， 需要依次执行.



### B0002_BeautifulSoup
解析 HTML 代码片段，获取其中的 文本内容。



### B0003_mysql_to_text
尝试将 mysql 的新闻表中，存储了 html 的字段的数据， 导出到 txt 文件中。




### B0004_postgres
访问 postgres 数据库的例子.
一种是使用 psycopg2 直接访问 postgres 数据库。
一种是使用 postgrest， 通过 postgrest 服务器，间接访问 postgres 数据库。




### B0005_Ollama
使用 ollama 库， 调用 Ollama 的例子。
hello_world.py 是等待全部响应都返回了，才输出结果。
hello_world2.py 是流式输出结果。



### B0006_Pandas
使用 Pandas 库的例子。
Pandas 是 Python 中一个强大的数据分析工具库，广泛应用于数据处理、清洗、分析和可视化。


### B0007_NumPy
使用 NumPy 库的例子。
NumPy提供了高效的数组操作和数学函数。

