from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartVitalTask
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.InformationSystem.VitalTask import VitalTaskSever
import time


routeKey = 'vitalTask'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：vitalTaskController
父类：baseController
描述：读取体征任务功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/19
"""

class vitalTaskController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:读取体征任务功能的Controller层实现
    @:date 2023/1/19
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def vitalTask(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的生命体征信息
        """
        retMess = 0
        try:
            # time.sleep(0.5)
            # 以下这一段基本上可以copy到所有json输入的非login的Controller代码中
            dataDict = {}
            for item in request.json:
                dataDict[item] = request.json[item] #将request中的信息读取出来
            token = request.headers.get('Authtoken') #获取请求标头中的auth-token

            userId, authCorrect = AuthSever.AuthSever().checkAuth(token) #校验auth-token是否正确
            print(userId)
            if(authCorrect != True):
                raise ValueError("Auth校验失败，请重新登录")
            # 以上是格式逻辑，以下开始功能实现

            # 用userID查表获得工作人员dto
            staff = Staff.Staff()
            staff.setStaffId(userId)
            checkStaffMessSever = CheckStaffMessSever.CheckStaffMessSever()
            staff = checkStaffMessSever.checkStaffMess(staff)
            # 用科室代码查询病人基础信息List
            departId = dataDict["departId"]
            departVitalTask = DepartVitalTask.DepartVitalTask()
            vitalTaskSever = VitalTaskSever.VitalTaskSever()
            departVitalTask.setStaff(staff)
            departVitalTask.setDepartId(departId)
            depart = vitalTaskSever.vitalTaskSever(departVitalTask)
            # 最终输出预处理
            depart.obj2Dict()
            retMess = depart.__dict__
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = vitalTaskController().fullPath #固定部分，不要删除