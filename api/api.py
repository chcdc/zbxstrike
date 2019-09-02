from flask import Flask
from flask_restful import Api, Resource
from resources.zbxstrike import Zbxstrike, Zbxstrike_list
from model.zbxstrike import ZbxstrikeModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

api = Api(app)

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(Zbxstrike_list, '/zbxstrike')
api.add_resource(Zbxstrike, '/zbxstrike/<string:zabbix_ip>')


if __name__=='__main__':
    from sql_alchemy import database
 
    database.init_app(app)
    app.run(debug=True, host='0.0.0.0')
