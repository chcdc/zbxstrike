from sql_alchemy import database

class ZbxstrikeModel(database.Model):
    __tablename__ = 'zbxstrike'

    zabbix_ip = database.Column(database.String, primary_key=True)
    zabbix_dns = database.Column(database.String(80))
    zabbix_user = database.Column(database.String(10))
    zabbix_password = database.Column(database.String(10))

    def __init__(self, zabbix_ip, zabbix_dns, zabbix_user, zabbix_password):
        self.zabbix_ip = zabbix_ip
        self.zabbix_dns = zabbix_dns
        self.zabbix_user = zabbix_user
        self.zabbix_password = zabbix_password

    def parse_json(self):
        return {'
            'zabbix_ip': self.zabbix_ip,
            'zabbix_dns': self.zabbix_dns
            'zabbix_user': self.zabbix_user
            'zabbix_password': self.zabbix_password
        '}

    def save_target(self):
        database.session.add(self)
        database.session.commit()

