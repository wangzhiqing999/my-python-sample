from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Union
import psycopg2
from psycopg2.extras import DictCursor

import uvicorn
from contextlib import contextmanager


app = FastAPI()


class SQLQuery(BaseModel):
    sql_query: str


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


@app.post("/execute_query")
async def execute_query(
    query: SQLQuery,
    api_key: Optional[str] = Header(None, alias="X-API-Key")
):
    """处理POST请求以执行SQL查询。"""
    try:
        sql_queries = query.sql_query.strip()

        
        print(sql_queries)
        # sql_queries 是外部传递进来的参数.
        # LLM 模型，可能会传递一些特殊的字符或标记，需要先移除掉.
        sql_queries = sql_queries.replace("```sql", "")
        sql_queries = sql_queries.replace("```", "")
        sql_queries = sql_queries.replace("###", "")
        sql_queries = sql_queries.replace("SQL 查询", "")


        if not sql_queries:
            raise HTTPException(status_code=400, detail="Missing sql_query parameter")


        with get_db_connection(app.db_config) as conn:
            results = []
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                for sql_query in sql_queries.split(';'):
                    if sql_query.strip():
                        print(sql_query)
                        cursor.execute(sql_query)
                        result = cursor.fetchall()
                        if result:
                            # 获取列名
                            columns = [desc[0] for desc in cursor.description]
                            # 将结果转换为字典列表
                            for row in result:
                                row_dict = dict(zip(columns, row))
                                results.append(row_dict)
                conn.commit()


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
        "options": "-c search_path=public"
    }


    # 添加API密钥配置
    app.api_key = "这里是API密钥"  # 建议使用环境变量存储此密钥


    uvicorn.run(app, host='0.0.0.0', port=35003)