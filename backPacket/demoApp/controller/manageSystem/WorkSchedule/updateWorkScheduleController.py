from flask import Blueprint, request
from ...manageSystem.manageBaseController import manageBaseController
from backPacket.demoApp.dto import Staff
from backPacket.demoApp.dto.manageSystem.WorkSchedule import WorkSchedule
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.manageSystem.DepartWorkSchedule.UpdateWorkScheduleSever import UpdateWorkScheduleSever
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'updateWorkSchedule'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateWorkScheduleController
父类：manageBaseController
描述：【管理员端】新建排班记录Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/28
"""

class updateWorkScheduleController(manageBaseController):
    def __init__(self):
        self.basePath = manageBaseController().manageBasePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:【管理员端】修改排班功能Controller层实现
    @:date 2023/4/27
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def updateWorkScheduleController(key=1):
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
            # 工作人员信息读取完毕，开始读取前端信息
            startTime = dataDict['startTime']
            endTime = dataDict['endTime']
            workStaffId = dataDict['workStaffId']
            workId = dataDict['workId']
            workStaffDepart = dataDict['workStaffDepart']

            startTime,endTime = UsefulTools().startAndEndTimeMandarin2Format(startTime,endTime,"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S")

            # 前端信息读取完毕，开始装载dto
            workSchedule = WorkSchedule()
            # startTime
            workSchedule.setStartTime(startTime)
            # endTime
            workSchedule.setEndTime(endTime)
            # workStaffId
            workSchedule.setWorkStaffId(workStaffId)
            # staff
            workSchedule.setStaff(staff)
            # workStaffDepart
            workSchedule.setWorkStaffDepart(workStaffDepart)
            # workID
            workSchedule.setWorkId(workId)
            # DTO装载完成，开始进入Sever层
            updateWorkScheduleSever = UpdateWorkScheduleSever()
            retMess = updateWorkScheduleSever.updateWorkSchedule(workSchedule)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateWorkScheduleController().fullPath #固定部分，不要删除