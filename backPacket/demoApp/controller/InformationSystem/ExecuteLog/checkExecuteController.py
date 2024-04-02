from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartExecute
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.InformationSystem.Execute import CheckExecuteSever
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'checkExecute'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：checkExecuteController
父类：baseController
描述：读取执行单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/31
"""

class checkExecuteController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:读取体征任务功能的Controller层实现
    @:date 2023/3/31
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def checkExecute(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的执行单信息
        """
        retMess = 0
        try:
            # 以下这一段基本上可以copy到所有json输入的非login的Controller代码中
            dataDict = {}
            for item in request.json:
                dataDict[item] = request.json[item] #将request中的信息读取出来
            token = request.headers.get('AuthToken') #获取请求标头中的auth-token
            userId, authCorrect = AuthSever.AuthSever().checkAuth(token) #校验auth-token是否正确
            if(authCorrect != True):
                raise ValueError("Auth校验失败，请重新登录")
            # 以上是格式逻辑，以下开始功能实现

            # 用userID查表获得工作人员dto
            staff = Staff.Staff()
            staff.setStaffId(userId)
            checkStaffMessSever = CheckStaffMessSever.CheckStaffMessSever()
            staff = checkStaffMessSever.checkStaffMess(staff)
            #

            # 用科室代码查询执行单信息
            departId = dataDict["departId"]
            startTime = dataDict["startTime"]
            endTime = dataDict['endTime']
            startTime,endTime = UsefulTools().null2Time(startTime,endTime,0,1)
            startTime,endTime = UsefulTools().startAndEndTimeMandarin2Format(startTime,endTime,"%Y-%m-%d","%Y年%m月%d日")
            departExecute = DepartExecute.DepartExecute()
            checkExecuteSever = CheckExecuteSever.CheckExecuteSever()
            departExecute.setDepartId(departId)
            departExecute.setStartTime(startTime)
            departExecute.setEndTime(endTime)
            departExecute.setStaff(staff)
            departExecute = checkExecuteSever.checkExecuteSever(departExecute)

            # 最终输出预处理
            departExecute.obj2Dict()
            retMess = departExecute.__dict__
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = checkExecuteController().fullPath #固定部分，不要删除