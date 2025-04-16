from mcp.server.fastmcp import FastMCP
import psycopg2
from psycopg2.extras import DictCursor
from contextlib import contextmanager
import logging
import json


logger = logging.getLogger("mcp")

settings = {
    "log_level": "DEBUG"
}

# 初始化mcp服务
mcp = FastMCP("hello-mcp-server", log_level="ERROR", settings=settings)



@contextmanager
def get_db_connection(config):
    """数据库连接的上下文管理器"""
    conn = None
    try:
        conn = psycopg2.connect(**config)
        yield conn
    finally:
        if conn:
            conn.close()





@mcp.tool(name="get_all_users", description="获取全部的用户")
async def get_all_users():


    sql_query = """SELECT 
	user_id, 
	user_code, 
	user_name, 
	user_avator
FROM 
	mr_user
"""

    with get_db_connection(mcp.db_config) as conn:
        results = []
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            if sql_query.strip():
                cursor.execute(sql_query)
                result = cursor.fetchall()
                if result:
                    # 获取列名
                    columns = [desc[0] for desc in cursor.description]
                    # 将结果转换为字典列表
                    for row in result:
                        row_dict = dict(zip(columns, row))
                        results.append(row_dict)
    return json.dumps(results)





@mcp.tool(name="get_user_by_login_code", description="获取指定“登录代码/登录名”的用户")
async def get_user_by_login_code(
    login_code: str
):
    sql_query = """SELECT 
    user_id, 
    user_code, 
    user_name, 
    user_avator
FROM 
    mr_user
WHERE
    user_code =  %(loginCode)s
"""

    with get_db_connection(mcp.db_config) as conn:
        results = []
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            if sql_query.strip():
                cursor.execute(sql_query, {'loginCode': login_code})
                result = cursor.fetchall()
                if result:
                    # 获取列名
                    columns = [desc[0] for desc in cursor.description]
                    # 将结果转换为字典列表
                    for row in result:
                        row_dict = dict(zip(columns, row))
                        results.append(row_dict)

    return json.dumps(results)



@mcp.tool(name="get_user_roles", description="获取指定ID的用户,所分配的角色")
async def get_user_roles(
    userid: int
):

    sql_query = """SELECT 
    r.role_id, 
    r.system_code, 
    r.role_code, 
    r.role_name 
FROM 
    mr_role r
      join mr_user_role mur on (r.role_id = mur.role_id)
where 
    mur.user_id = %(userid)s
"""

    with get_db_connection(mcp.db_config) as conn:
        results = []
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            if sql_query.strip():
                cursor.execute(sql_query, {'userid': userid})
                result = cursor.fetchall()
                if result:
                    # 获取列名
                    columns = [desc[0] for desc in cursor.description]
                    # 将结果转换为字典列表
                    for row in result:
                        row_dict = dict(zip(columns, row))
                        results.append(row_dict)
    return json.dumps(results)





def run():
    # 运行后，尝试用浏览器打开 http://localhost:8000/sse 看看能否有结果.
    mcp.run(transport="sse")



if __name__ == '__main__':

    # 数据库配置
    mcp.db_config = {
        "database": "postgres",
        "user": "postgres",
        "password": "这里是测试数据库的密码",
        "host": "pve002",
        "port": "5432",
        "options": "-c search_path=dbo"
    }

    run()
