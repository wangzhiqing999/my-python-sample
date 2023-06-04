

远程服务器， mysql 导出一个比较大的 sql 文件， 压缩后，复制到本地。
解压缩后，准备将其导入本地的服务器。



然而，在使用下面的方式，执行那个 sql 文件时，出错了。
mysql.exe -h  mySQL服务器地址  -u用户 -p密码 --database=数据库名 < 需要执行的脚本.sql


结果是表创建了，  数据只插入了一部分。

简单打开 sql 文件分析具体是那里出错了，非常麻烦。
因为那个 sql 文件，有 600多兆。



使用 python，写2个脚本。

cut_dump_file.py  负责将那个大的 sql 文件，拆分为多个小的 sql 文件.

insert_dump_file.py  负责依次执行 小的 sql 文件.


