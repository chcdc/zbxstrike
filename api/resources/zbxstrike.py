import sqlite3
from flask_restful import Resource, reqparse
from model.zbxstrike import ZbxstrikeModel

class Zbxstrike(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('zabbix_ip', type=str, required=True)
    arguments.add_argument('zabbix_dns', type=str, required=True)
    arguments.add_argument('zabbix_user', type=str, required=True)
    arguments.add_argument('zabbix_password', type=str, required=True)

    def get(self):
        pass
    
    def post(self, zabbix_ip):
        data = Zbxstrike.arguments.parse_args()
        zbxstrike = ZbxstrikeModel(zabbix_ip, **data)

        try:
            zbxstrike.save()
        except:
            return {'message': 'Internal server error'}, 500
        
        return zbxstrike.parse_json()