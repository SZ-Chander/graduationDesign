from backPacket.demoApp.dto import User
from flask import current_app
from sqlalchemy import text
import time
"""
类名：AuthDao
描述：auth令牌保存和读取功能Dao层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/19
备注：为了保证线程安全，使用数据库存放令牌。
"""
class AuthDao:
    def __init__(self):
        self.tableName = "sys_user_token"
        self.db = current_app.config['db']

    """
    功能阐述:auth-token保存,本功能过于特殊，因此不使用dto传参。
    @:date 2023/1/19
    @:author 常舜志
    """
    def saveAuth(self,inputToken,userId):
        """
        :param inputToken: 传入的令牌，类型为String
        :param userId: 传入的用户id，类型为int
        :return: 报错或True，类型为Exception或Boolen
        """
        try:
            date = time.time()
            sqlStr = "insert into {} values ('{}',{},'{}')".format(self.tableName,inputToken,date,userId)
            self.db.engine.execute(sqlStr)
            return True
        except Exception as e:
            return e

    """
    功能阐述: auth-token校验，本功能过于特殊因此不使用dto传参。
    @:date 2023/1/19
    @:author 常舜志
    """
    def checkAuth(self,data):
        """
        :param data: 输入的auth解析数据，类型为Dict
        :return: 报错或数据行计数，类型为Exception或int
        """
        try:
            sqlStr = "select pwd from sys_user where userId='{}'".format(data['id'])
            retStr = (list(self.db.engine.execute(sqlStr)))[0][0]
            return retStr
        except Exception as e:
            return e
