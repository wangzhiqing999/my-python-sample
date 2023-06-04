import os
import pymysql
import traceback

"""
执行 拆分后文件的处理.
数据库工具导出的 sql 文件，超大。
由多个 INSERT INTO 语句组成。
每个 INSERT INTO 语句， 大小为 1M .

前置的代码，已经将一个大文件，拆分为多个小文件。
每个小文件，只有1行 INSERT INTO 语句，大小为 1M。

这个代码，将依次执行每个小文件。

"""








def insert_dump_file(file_path):

    # 打开数据库连接
    db = pymysql.connect(host='数据库 ip 地址',
                         user='用户名',
                         password='密码',
                         database='数据库名',
                         charset='utf8' )
     
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
     
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")
     
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print ("Database version : %s " % data)


    try:

        # 拆分索引.
        index = 1

        while os.path.exists(f'{file_path}_{index}.sql'):
            # 文件存在的情况下，就尝试执行.
            print (f'{file_path}_{index}')
            with open(f'{file_path}_{index}', 'r', encoding='utf-8') as f:
                first_line = f.readline()
                cursor.execute(first_line)
                # 文件太多， 憋到最后再提交的话，也是麻烦，这里就一个文件提交一次。
                db.commit()

            # 切换到下一个子文件.
            index = index + 1

    except:
        # 如果发生错误则回滚    
        db.rollback()   
        
        print ("error...")
        traceback.print_exc()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()




insert_dump_file("my_news_detail");


