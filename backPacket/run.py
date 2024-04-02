# -*- coding: utf-8 -*-
from flask import Flask
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, render_template
import sys

sys.path.append('..')
from backPacket.demoApp import controller
# import baseController

import os
import importlib

"""
类名：mainEnter
描述：程序主入口
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/13
备注：主入口，程序运行必须实例化本类后使用
"""


class mainEnter:
    """
    功能阐述:初始化主入口，并调用工厂函数
    @:date 2023/1/13
    @:author 常舜志
    """

    def __init__(self):
        self.app = controller.create_app()  # 初始化工厂函数

    """
    功能阐述:程序执行器
    @:date 2023/1/13
    @:author 常舜志
    """

    def run(self):
        self.app.run(debug=False)  # 执行，True为可调试状态

    """
    功能阐述:蓝图注册器
    @:date 2023/1/13
    @:author 常舜志
    """

    def routeRegister(self, inputRoute, apiPath):
        """
        :param inputRoute: Controller的蓝图注册，类型为flask.Blueprint
        :param apiPath: Controller的完整文件路径，类型为String
        :return: function(x),在app中对进行Controller的路径进行蓝图注册
        """
        self.app.register_blueprint(inputRoute, url_prefix=apiPath)  # 注册蓝图

    """
    功能阐述:实际的程序运行方法和主入口
    @:date 2023/1/13
    @:author 常舜志
    """

    def forword(self):
        """
        :return: 启动app
        """
        controllerPacketList = controller.getAllController()  # 路径收集器
        for controllerPacket in controllerPacketList:
            # packetName = "{}()".format(controllerPacket.split('.')[-1])
            packet = importlib.import_module(controllerPacket)  # 路由收集器
            self.routeRegister(packet. api_route, packet.fullPath)  # 调用蓝图注册器
        self.mk_index()
        self.run()

    def mk_index(self):
        app = self.app

        @app.route('/')
        def index():
            try:
                return render_template('index.html', name='index')  # 前端包启动
            except:
                return dict(web="启动失败")


if __name__ == '__main__':
    enter = mainEnter()
    enter.forword()
