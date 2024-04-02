from flask import Blueprint
import backPacket.demoApp.controller.baseController

routeKey = 'manage'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除
"""
类名：manageBaseController
父类：baseController
描述：管理系统父类的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
"""
class manageBaseController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.manageBasePath = super().makeFullPath() #固定写法，不要删除

fullPath = manageBaseController().manageBasePath