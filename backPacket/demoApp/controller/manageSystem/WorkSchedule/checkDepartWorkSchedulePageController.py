from flask import Blueprint, request
from ...manageSystem.manageBaseController import manageBaseController
from backPacket.demoApp.dto import Staff
from backPacket.demoApp.dto.manageSystem.WorkSchedule import WorkSchedule
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.manageSystem.DepartWorkSchedule.CheckDepartWorkSchedulePageSever import CheckDepartWorkSchedulePageSever
import datetime
from backPacket.demoApp.tools.usefulTools import UsefulTools
import time

routeKey = 'checkDepartWorkSchedulePage'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：checkDepartWorkSchedulePageController
父类：manageBaseController
描述：读取执行单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/29
"""

class checkDepartWorkSchedulePageController(manageBaseController):
    def __init__(self):
        self.basePath = manageBaseController().manageBasePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:【管理员端】排班信息的Controller层实现
    @:date 2023/4/19
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def checkDepartWorkSchedulePage(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的执行单信息
        """
        retMess = 0
        try:
            # time.sleep(0.5)
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

            departId = dataDict["departId"]
            startTime = dataDict['checkInputStartTime']
            endTime = dataDict['checkInputEndTime']
            if(departId == None):
                departId = staff.getDepartCode()[0]
            if(startTime == None):
                startTime = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d")
            workSchedule = WorkSchedule()
            if(endTime == None):
                endTime = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

            startTime,endTime = UsefulTools().startAndEndTimeMandarin2Format(startTime,endTime,"%Y-%m-%d","%Y年%m月%d日")
            workSchedule.setStaff(staff)
            workSchedule.setDepartId(departId)
            workSchedule.setStartTime(startTime)
            workSchedule.setEndTime(endTime)
            checkDepartWorkSchedulePageSever = CheckDepartWorkSchedulePageSever()
            retMess = checkDepartWorkSchedulePageSever.CheckDepartWorkSchedulePage(workSchedule).__dict__
            retMess['checkInputStartTime'] = startTime
            retMess['checkInputEndTime'] = endTime
            retMess['departId'] = departId
            if(len(retMess) == 2):
                raise ValueError("查询失败，请检查数据！")


        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = checkDepartWorkSchedulePageController().fullPath #固定部分，不要删除