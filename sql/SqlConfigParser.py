import configparser


class SqlConfigParser(object):
    host = ""
    user = ""
    password = ""
    charset = ""
    db = ""

    # 定义构造函数
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("./sql/sql.ini")
        self.host = host = cf.get("Mysql-Database", "host")  # 获取[Mysql-Database]中host对应的值
        self.user = host = cf.get("Mysql-Database", "user")
        self.password = host = cf.get("Mysql-Database", "password")
        self.db = host = cf.get("Mysql-Database", "db")
        self.charset = host = cf.get("Mysql-Database", "charset")
