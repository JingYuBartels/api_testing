from pymysql import cursors, connect
from os.path import abspath, dirname, join
import configparser as cparser
from pymysql.err import OperationalError

#==============read db_config.ini==============

base_dir = dirname(dirname(abspath(__file__)))
file_path = join(base_dir, 'dev.ini')
print(file_path)

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')

# ==================encapsulation SQL basic operation===========================
class DB:
    def __init__(self):
        try:
            self.connection = connect(host=host,
                                      port=int(port),
                                      user=user,
                                      password=password,
                                      db=db,
                                      charset='utf8mb4',
                                      cursorclass=cursors.DictCursor)
        except OperationalError as e:

            print('Mysql Error {}: {}'.format(e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "DELETE FROM " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
            print(real_sql)
        self.connection.commit()

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())
        print(key)
        value = ','.join(table_data.values())
        print(value)
        real_sql = 'INSERT INTO ' + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    db = DB()
    table_name = 'sign_event'
    data = {'id': 12, 'name': 'hongmi', '`limit`': 2000, 'status': 1, 'address': 'Beijing exhibition center', 'start_time': '2019-08-20 00:25:42'}

    db.clear(table_name)
    # db.insert(table_name, data)
    db.close()

