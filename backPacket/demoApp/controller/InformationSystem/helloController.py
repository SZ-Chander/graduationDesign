from flask import Blueprint, request
import backPacket.demoApp.controller.baseController

routeKey = 'hello'
api_route = Blueprint(routeKey, __name__)

"""
类名：helloController
描述：Controller子类实现测试demo
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/13
备注：本类仅作为测试使用，不作实用，在测试时可以随意修改，因此不做注释
"""
class helloController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath
        self.plusPath = routeKey
        self.fullPath = super().makeFullPath()

    @api_route.route('/<username>', methods=['GET'])
    def baseController(username):
        print("hello")
        return dict(hello=username)

    def hello(self):
        print("hello")

fullPath = helloController().fullPath