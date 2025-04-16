from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union
import psycopg2
from psycopg2.extras import DictCursor

import uvicorn
from contextlib import contextmanager


app = FastAPI()



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


@app.get("/get_all_users")
async def get_all_users(api_key: Optional[str] = Header(None, alias="X-API-Key")):
    try:
        if verify_api_key(api_key) is False:
            raise HTTPException(status_code=401, detail="Unauthorized")

        sql_query = """SELECT 
	user_id, 
	user_code, 
	user_name, 
	user_avator
FROM 
	mr_user
"""

        with get_db_connection(app.db_config) as conn:
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
        return results

    except psycopg2.ProgrammingError as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")



@app.get("/get_user_by_login_code")
async def get_user_by_login_code(
    login_code: str,
    api_key: Optional[str] = Header(None, alias="X-API-Key")
):
    try:
        if verify_api_key(api_key) is False:
            raise HTTPException(status_code=401, detail="Unauthorized")

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

        with get_db_connection(app.db_config) as conn:
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
        return results

    except psycopg2.ProgrammingError as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")



@app.get("/get_user_roles")
async def get_user_roles(
    userId: int,
    api_key: Optional[str] = Header(None, alias="X-API-Key")
):
    try:
        if verify_api_key(api_key) is False:
            raise HTTPException(status_code=401, detail="Unauthorized")

        sql_query = """SELECT 
    r.role_id, 
    r.system_code, 
    r.role_code, 
    r.role_name 
FROM 
    mr_role r
      join mr_user_role mur on (r.role_id = mur.role_id)
where 
    mur.user_id = %(userId)s
"""

        with get_db_connection(app.db_config) as conn:
            results = []
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                if sql_query.strip():
                    cursor.execute(sql_query, {'userId': userId})
                    result = cursor.fetchall()
                    if result:
                        # 获取列名
                        columns = [desc[0] for desc in cursor.description]
                        # 将结果转换为字典列表
                        for row in result:
                            row_dict = dict(zip(columns, row))
                            results.append(row_dict)
        return results

    except psycopg2.ProgrammingError as e:
        raise HTTPException(status_code=500, detail=f"数据库错误: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")






def verify_api_key(api_key: Optional[str]) -> bool:
    """验证API密钥"""
    return api_key == app.api_key



if __name__ == '__main__':
    # 数据库配置
    app.db_config = {
        "database": "postgres",
        "user": "postgres",
        "password": "这里是测试数据库的密码",
        "host": "pve002",
        "port": "5432",
        "options": "-c search_path=dbo"
    }


    # 添加API密钥配置
    app.api_key = "API密钥"  # 建议使用环境变量存储此密钥


    uvicorn.run(app, host='0.0.0.0', port=35003)