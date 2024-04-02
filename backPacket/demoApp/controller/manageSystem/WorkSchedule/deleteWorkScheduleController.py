from flask import Blueprint, request
from ...manageSystem.manageBaseController import manageBaseController
from backPacket.demoApp.dto import Staff
from backPacket.demoApp.dto.manageSystem.WorkSchedule import WorkSchedule
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.manageSystem.DepartWorkSchedule.DeleteWorkScheduleSever import DeleteWorkSchedule
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'deleteWorkSchedule'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：deleteWorkScheduleController
父类：manageBaseController
描述：【管理员端】删除排班记录Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/5/23
"""

class deleteWorkScheduleController(manageBaseController):
    def __init__(self):
        self.basePath = manageBaseController().manageBasePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:【管理员端】创建账号的Controller层实现
    @:date 2023/5/23
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def deleteWorkSchedule(key=1):
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
            workId = dataDict['workId']
            endTime = dataDict['endTime']
            departId = dataDict['departId']

            usefulTools = UsefulTools()
            endTime = usefulTools.mandarinDate2Format(endTime,"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S")

            # 前端信息读取完毕，开始装载dto
            workSchedule = WorkSchedule()
            # workId
            workSchedule.setWorkId(workId)
            # endTime
            workSchedule.setEndTime(endTime)
            # staff
            workSchedule.setStaff(staff)
            # departId
            workSchedule.setWorkStaffDepart(departId)
            # DTO装载完成，开始进入Sever层
            deleteWorkSchedule = DeleteWorkSchedule()
            retMess = deleteWorkSchedule.deleteWorkSchedule(workSchedule)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = deleteWorkScheduleController().fullPath #固定部分，不要删除