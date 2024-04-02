import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
import os
from backPacket.demoApp import config
from flask_cors import CORS


"""
功能阐述:Flask工厂函数
@:date 2023/1/13
@:author 常舜志
"""
def create_app():
    """
    :return: app 工厂创建的flask app
    """
    # 生成WebApp
    distPath = os.path.dirname(__file__).replace("controller","dist")
    app = Flask(__name__,static_folder=distPath,template_folder=distPath,static_url_path="")
    CORS(app, supports_credentials=True)
    sqlConfig = config.getConfig()['sqlConfig']
    db_URI = "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(sqlConfig['user'],sqlConfig['password'],
                                                               sqlConfig['host'],sqlConfig['dataBaseName'])#写死的sql-sever格式，若希望实现数据库的模块化，需要在配置文件里直接写uri
    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = db_URI  # 使用flask的app注册uri
        db = SQLAlchemy(app)  # 数据库实现
        db.create_all()  # 固定写法
        app.config['db'] = db
    webApp = app
    return app

"""
功能阐述:Controller蓝图注册获取器
@:date 2023/1/18
@:author 常舜志
"""
def getAllController():
    """
    :return: retList 返回的信息Controller文件路径列表，类型为list<str>
    """
    controllerPath = __name__.replace('.','/').replace('backPacket/','')
    pathList = findPyFilesFromDir(controllerPath)
    return pathList

def findPyFilesFromDir(dirPath:str):
    pathList = []
    for subPath in os.listdir(dirPath):
        fullSubPath = "{}/{}".format(dirPath,subPath)
        if(os.path.isdir(fullSubPath)):
            subList = findPyFilesFromDir(fullSubPath)
            pathList += subList
        else:
            if(fullSubPath.split('.')[-1] == 'py'):
                fileName = fullSubPath.split('backPacket/')[-1]
                if ("Controller" in fileName):
                    pathList.append("backPacket.{}".format(fileName).replace("/",'.').replace('.py',''))
    return list(set(pathList))