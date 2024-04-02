from flask import Blueprint
from backPacket.demoApp import config
from backPacket.demoApp import sever

routeKey = 'base'
api_route = Blueprint(routeKey, __name__)

"""
类名：baseController
描述：Controller基类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/13
备注：所有Controller层都必须继承此类，因此详细功能尽可能在子类中实现。
"""
class baseController:
    def __init__(self):
        self.basePath = 'api'
        self.plusPath = None
        self.fullPath = self.makeFullPath()

    """
    功能阐述:获取完整的Controller类api路径
    @:date 2023/1/13
    @:author 常舜志
    """
    def makeFullPath(self):
        """
        :return: 完整的Controller类api路径，类型为string
        """
        if(self.plusPath == None):
            retStr = "/{}".format(self.basePath)
        else:
            retStr = "/{}/{}".format(self.basePath,self.plusPath)
        return retStr

    """
    功能阐述:测试demo，不作为实际使用功能
    @:date 2023/1/13
    @:author 常舜志
    """
    @api_route.route('/<username>', methods=['GET'])
    def baseController(username):
        """
        :return: 格式化的输入变量，类型为dict
        """
        print("base")
        return dict(name=username)

fullPath = baseController().fullPath