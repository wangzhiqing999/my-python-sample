import os
import pymysql
import traceback
from bs4 import BeautifulSoup


"""
脚本处理内容。

1. 从 mysql 数据库读取数据.
2. 将字段中的 html 代码片段， 解析为 text 文本.
3. 输出为 txt 文件.


目的：是将数据库中的数据，导出为 txt 文本，然后拿去给其他的系统，做知识库的生成操作。

"""



def exp_db_to_txt_file():


    # 打开数据库连接
    db = pymysql.connect(host='数据库 ip 地址',
                         user='用户名',
                         password='密码',
                         database='数据库名',
                         charset='utf8' )

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()


    # 预期是 一天的数据，存储到一个 txt 文件当中。
    # 测试的时候，limit 5
    # 正式使用时，将其注释掉.
    sql = """
SELECT
    CONCAT(nt.news_type_name, DATE_FORMAT(nd.news_datetime, '_%Y年%m月%d日'), '.txt') as file_name,
    nd.news_title,
    nd.news_html
FROM
    my_news_type nt
        join  my_news_detail nd  on (nt.news_type_code = nd.news_type_code)
WHERE
    nt.news_type_code = 'caifuhao_5'
/* limit 5  */
"""


    try:

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)

        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            file_name = row[0]
            news_title = row[1]
            news_html = row[2]
            print ("file_name=%s,news_title=%s" %(file_name, news_title))

            # 以 “追加” 的方式，打开文件。
            with open(file_name, 'a', encoding='utf-8') as output_file:
                # 先写入一行 标题。
                output_file.write(news_title + "\n")

                # 解析 HTML 片段.
                soup = BeautifulSoup(news_html, 'lxml')

                # 写入后续的 HTML 转换为 文本的信息.
                for p in soup.find_all("p"):
                    text = p.get_text()
                    text = text.strip()
                    if len(text) > 0 :
                        output_file.write(text + "\n")
                        
                output_file.write("\n")



    except:
        print ("error...")
        traceback.print_exc()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()





exp_db_to_txt_file()