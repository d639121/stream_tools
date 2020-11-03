#!/usr/bin/python
# @Time    : 2020/3/25 15:58
# @Author  : LOUIE
# @Desc  : 数据库连接操作

from common.config_log import log
from config.read_config import rc
import pymysql


class ConfigDB:

    def __init__(self):
        self.host = rc.get_db("host")
        self.port = rc.get_db("port")
        self.user = rc.get_db("user")
        self.password = rc.get_db("password")
        # self.cursor = None

    def connect_db(self):

        try:
            self.db = pymysql.connect(host=self.host, port=int(self.port), user=self.user, password=self.password)
            self.cursor = self.db.cursor()
            print('###### DB connected success')
        except ConnectionError as e:
            print('Error: DB Connected Error !!')
            log.error('Error: DB Connected Error !!', exc_info=True)
            raise e
        except Exception as e:
            log.error("Error: 数据库连接时发生错误, 信息: %s" %e, exc_info=True)
            raise e

    def execute_sql(self, sql, params, num=1):

        self.connect_db()
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchmany(num)
            self.db.commit()
            return result
        except Exception as e:
            self.db.rollback()
            log.error("ERROR: 执行SQL语句时发生错误, 信息: %s" %e, exc_info=True)
        finally:
            self.cursor.close()

    def close_db(self):

        self.db.close()
        print("###### Database closed!")
        log.info("###### 正在关闭数据库连接 /////")


db = ConfigDB()


if __name__ == '__main__':
    result = db.execute_sql("SELECT `class_id`,`teach_schedule`,`gmt_create`,`gmt_modified` FROM `after_sale`.`after_sales_class_config` WHERE `class_id`='17257';")
    print(result)