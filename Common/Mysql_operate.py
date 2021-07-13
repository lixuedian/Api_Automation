# -*- coding: utf-8 -*-
# 开发团队 ： 平台研发部—测试组
# 开发时间 ： 2020/12/17 11:31
# 文件名称 ： Mysql_operate.py
# 开发工具 ： PyCharm
import pymysql
import os
import Common.Read_data
from Common.Log import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class MysqlDb(object):

    def __init__(self, db_conf):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = pymysql.connect(**db_conf, autocommit=True)
        # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        return data

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


# 读取配置参数
def mysql_conf(conf):
    data_file_path = os.path.join(BASE_PATH, "config", "Config.ini")
    data = Common.Read_data.data.load_ini(data_file_path)[f'{conf}']
    DB_CONF = {
        "host": data["mysql_host"],
        "port": int(data["mysql_port"]),
        "user": data["mysql_user"],
        "password": data["mysql_passwd"],
        "db": data["mysql_db"]
    }
    return DB_CONF


# 获取多个id列表
def mysql_id(mysql):
    DB_CONF = mysql_conf('mysql')
    # mysql = "select id from test_mp_goods_center.goods_handout where name = '测试_xuejian01'"
    Ids = MysqlDb(DB_CONF).select_db(mysql)
    a = []
    for handoutId in Ids:
        for handout in handoutId.values():
            a.append(handout)
    return a


# 测试库
def mysql_select(mysql):
    DB_CONF = mysql_conf('mysql')
    return MysqlDb(DB_CONF).select_db(mysql)
