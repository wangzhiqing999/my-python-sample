from postgrest import SyncPostgrestClient



class test_postgrest:

    def __init__(self):
        self.client = SyncPostgrestClient("http://pve002:3000", schema="dbo")


    def test_select(self):
        r = self.client.from_("mr_system").select("system_code, system_name, display_order").eq("system_code","TEST").execute()
        systemDatas = r.data
        print(systemDatas);


    def test_insert(self):        
        self.client.from_("mr_system").insert({'system_code': 'TEST', 'system_name': 'TEST', 'display_order': 100, 'system_icon': 'test-icon', 'remark': '-', 'status': 'ACTIVE', 'create_user': 'tester', 'create_time': '2023-06-08', 'last_update_user': 'tester', 'last_update_time': '2023-06-08'}).execute()
        print("-----insert finish-----")
    

    def test_update(self):
        self.client.from_("mr_system").update({"system_name": "TEST12345", "display_order": 123}).eq("system_code", "TEST").execute()
        print("-----update finish-----")



    def test_delete(self):
        self.client.from_("mr_system").delete().eq("system_code", "TEST").execute()
        print("-----delete finish-----")




tester = test_postgrest()
tester.test_select()


tester.test_insert()
tester.test_select()


tester.test_update()
tester.test_select()


tester.test_delete()
tester.test_select()


