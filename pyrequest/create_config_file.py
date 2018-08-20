from configparser import ConfigParser

config = ConfigParser()
config['mysqlconf'] = {
    'host': '127.0.0.1',
    'port': '8889',
    'user': 'root',
    'password': 'root',
    'db_name': 'guest_test'
}

with open('./dev.ini', 'w') as f:
    config.write(f)