import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS zbxstrike (zabbix_ip text PRIMARY KEY,\
                zabbix_dns text, zabbix_user text, zabbix_password text)"


cursor.execute(create_table)
connection.commit()
connection.close()

