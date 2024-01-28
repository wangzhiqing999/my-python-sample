import os
import sys
import pymysql
import traceback

"""
运行某个目录下，所有的 sql 文件.
"""








def run_sql_file(path):

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

        with os.scandir(path) as entries:
            for entry in entries:  
                if (entry.is_file()):
                    file_path = entry.path
                    # 尝试执行.
                    print (f'{file_path}')
                    # 读取 sql 文件，发现有 \ufeff 的情况下， 使用 utf-8-sig 来代替 utf-8
                    with open(file_path,encoding='utf-8-sig',mode='r') as f:
                        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
                        sql_list = f.read().split(';')[:-1]
                        for x in sql_list:
                            # 判断包含空行的
                            if '\n' in x:
                                # 替换空行为1个空格
                                x = x.replace('\n', ' ')
                 
                            # 判断多个空格时
                            if '    ' in x:
                                # 替换为空
                                x = x.replace('    ', '')
                 
                            # sql语句添加分号结尾
                            sql_item = x+';'
                            # print(sql_item)
                            cursor.execute(sql_item)
                            print("执行成功sql: %s"%sql_item)

    except:
        # 如果发生错误则回滚    
        db.rollback()   
        
        print ("error...")
        traceback.print_exc()

    finally:
        # 关闭游标连接
        cursor.close()
        db.commit()
        # 关闭数据库连接
        db.close()








def run_all_sql_file():

    if (len(sys.argv) == 1):
        print("需要指定 sql 文件所在的目录！")
    else:
        run_sql_file(sys.argv[1])



run_all_sql_file()





