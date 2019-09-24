import threading
import pymysql

from sql.SqlConfigParser import SqlConfigParser


class SqlConnector(object):
    _lock = threading.Lock()

    def __init__(self):
        parser = SqlConfigParser()
        self.__sql_conn = pymysql.connect(host=parser.host, user=parser.user, password=parser.password,
                                          database=parser.db,
                                          charset=parser.charset)
        self.__cursor = self.__sql_conn.cursor()

    def __new__(cls, *args, **kwargs):
        if not hasattr(SqlConnector, "_instance"):
            with SqlConnector._lock:
                if not hasattr(SqlConnector, "_instance"):
                    SqlConnector._instance = object.__new__(cls)
        return SqlConnector._instance

    def execute(self, sql, data):
        self.__cursor.execute(sql, data)
        self.__sql_conn.commit()

    def close(self):
        # 关闭光标对象
        self.__cursor.close()
        # 关闭数据库连接
        self.__sql_conn.close()
