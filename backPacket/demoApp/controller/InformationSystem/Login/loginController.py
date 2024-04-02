from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import User
from backPacket.demoApp.sever.InformationSystem.Login import LoginSever
from backPacket.demoApp.tools.ownHandler import JsonHandler

routeKey = 'login'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：loginController
父类：baseController
描述：登录功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/13
"""

class loginController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:登录功能的Controller层主入口
    @:date 2023/1/13
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def login(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的用户信息
        """
        retMess = 0
        try:
            userDict = {}
            for item in request.json:
                userDict[item] = request.json[item]
            user = User.User()
            user.setUserFromDict(userDict)
            loginSever = LoginSever.LoginSever()
            retUser = loginSever.login(user)
            if (Exception in retUser.__class__.__bases__):
                retMess = retUser
            else:
                retMess = retUser.__dict__
        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)

fullPath = loginController().fullPath #固定部分，不要删除