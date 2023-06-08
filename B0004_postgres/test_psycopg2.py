import psycopg2


class test_psycopg2:

    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="这里是测试数据库的密码",
            host="pve002",
            port="5432")
        print("Opened database successfully")


    def __del__(self):
        self.conn.close()
        print("Close database conn...")


    def test_select(self):
        cur = self.conn.cursor()
        cur.execute("SELECT system_code, system_name, display_order  FROM dbo.mr_system WHERE system_code = 'TEST'")
        rows = cur.fetchall()
        for row in rows:
            print("system_code = ", row[0])
            print("system_name = ", row[1])
            print("display_order = ", row[2])
        print("-----select finish-----")


    def test_insert(self):
        cur = self.conn.cursor()
        sql = """INSERT INTO dbo.mr_system (
                system_code, system_name, display_order, 
                system_icon, remark, status, 
                create_user, create_time, last_update_user, 
                last_update_time
            ) VALUES(
                'TEST', '测试', 100, 
                'test_icon', '-', 'ACTIVE', 
                'tester', localtimestamp, 'tester', 
                localtimestamp
            )"""

        cur.execute(sql)        
        print("-----insert finish-----")
    

    def test_update(self):
        cur = self.conn.cursor()
        sql = """UPDATE dbo.mr_system 
                SET 
                    system_name = '测试名称',
                    display_order = 123
            WHERE
                system_code = 'TEST'
            """

        cur.execute(sql)        
        print("-----update finish-----")



    def test_delete(self):
        cur = self.conn.cursor()
        sql = """DELETE FROM dbo.mr_system 
            WHERE
                system_code = 'TEST'
            """

        cur.execute(sql)        
        print("-----delete finish-----")


tester = test_psycopg2()
tester.test_select()


tester.test_insert()
tester.test_select()


tester.test_update()
tester.test_select()


tester.test_delete()
tester.test_select()

del(tester)
