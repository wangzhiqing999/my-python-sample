import os
import codecs

"""
拆分文件的处理.
数据库工具导出的 sql 文件，超大。
由多个 INSERT INTO 语句组成。
每个 INSERT INTO 语句， 大小为 1M .

这个代码，将一个超大的 sql 文件， 拆分为多个 小文件。
每个小文件，最终为 1M 的样子.
"""


def cut_dump_file(file_path):
    with open(f'{file_path}.sql',  mode='r', encoding='utf-8') as f:
        chunk = f.readline()
        index = 1
        while chunk:
            if(chunk.startswith("INSERT INTO")):
                with open(f'{file_path}_{index}.sql', 'w', encoding='utf-8') as chunk_file:
                    chunk_file.write(chunk)
                index += 1            
            chunk = f.readline()


cut_dump_file("my_news_detail");