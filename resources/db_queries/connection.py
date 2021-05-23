from pypyodbc import connect

from resources.modules.config import db_login, db_host, db_name, db_pass


class db_cursor:
    def __init__(self, dbin):
        self.conn = connect(dbin)
        self.cursor = self.conn.cursor()

    def q_execute(self, query):
        self.cursor.execute(query)
        res = self.cursor.fetchall()
        return res

    def insert(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return 'success'


db_init = 'Driver={SQL Server};Server=%s;Database=%s;uid=%s;pwd=%s' % (
    db_host, db_name, db_login, db_pass)
db = db_cursor(db_init)
