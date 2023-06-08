## 测试库/表.

Host：pve002
Database: postgres
Schema: dbo
Table: 

CREATE TABLE dbo.mr_system (
	system_code varchar(32) NOT NULL,
	system_name varchar(64) NOT NULL,
	display_order int4 NULL,
	system_icon varchar(64) NULL,
	remark varchar(2048) NULL,
	status varchar(16) NULL,
	create_user varchar(64) NULL,
	create_time timestamp NOT NULL,
	last_update_user varchar(64) NULL,
	last_update_time timestamp NOT NULL,
	CONSTRAINT "PK_dbo.mr_system" PRIMARY KEY (system_code)
);



## Postgrest 服务

Host：pve002
Port：3000





## 使用 psycopg2

安装：
pip install psycopg2





## 使用 postgrest

安装：
pip install postgrest




