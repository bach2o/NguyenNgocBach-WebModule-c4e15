
import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds249818.mlab.com:49818/kebopdaividai

host = "ds249818.mlab.com"
port = 49818
db_name = "kebopdaividai"
user_name = "admin"
password = "123456"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
