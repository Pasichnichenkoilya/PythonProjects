import sqlite3


class Database:
    def __init__(self, db_name):
        self._db_name_ = db_name

    def execute_sql(self, command):
        conn = sqlite3.connect(self._db_name_)
        curs = conn.cursor()
        curs.execute(command)
        conn.commit()
        fetch_data = curs.fetchall()
        curs.close()
        conn.close()
        return fetch_data
