from backPacket.demoApp.dto import User
from flask import Flask, current_app
from sqlalchemy import text
"""
类名：LoginDao
描述：登录功能Dao层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/16
备注：1月16日更新，将登录改为了参数化查询的方式，可以防止注入式攻击
"""
class LoginDao:
    def __init__(self):
        self.tableName = "sys_user"
        self.db = current_app.config['db']

    """
    功能阐述:登录功能Dao层主入口（参数查询版）
    @:date 2023/1/16
    @:author 常舜志
    """
    def login(self, user):
        """
        :param user: 从Sever层传入的用户实体，类型为dto.User
        :return: userList: 返回Sever层的用户实体列表，类型为list<dto.User>
        """
        try:
            sqlStr = "select * from {} where userId=:userId".format(self.tableName)

            retData = list(self.db.engine.execute(text(sqlStr),dict(userId=user.id)))
            userList = []
            for userData in retData:
                _user = User.User()
                _user.setUser(None,password=userData[1], id=userData[2], autority=userData[3])
                userList.append(_user)
            return userList
        except Exception as e:
            return e
