import mariadb
import traceback


class BaseMariaDb(object):
    def __init__(self):
        self.connect = None
        self.cursor = None

    def _connect_db(self):
        self.connect = mariadb.connect(
            user="root",
            password="root123!",
            host="localhost",
            port=3306,
            database="ant_today_lotto"
        )

        self.cursor = self.connect.cursor(dictionary=True)

    def _close(self):
        self.connect.close()

    def exec_query(self, sql, params, with_commit=False):
        try:
            self._connect_db()

            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)

            if with_commit:
                db_result = None
                self.connect.commit()
            else:
                db_result = self.cursor.fetchall()

            self._close()

            return db_result
        except mariadb.Error as e:
            print(traceback.format_exc())
            print(f"Error connecting to MariaDB Platform: {e}")
