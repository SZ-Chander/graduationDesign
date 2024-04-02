from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartExecute,Execute
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.InformationSystem.Execute import InsertExecuteSever

routeKey = 'insertExecute'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertExecuteController
父类：baseController
描述：更新执行单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/4
"""

class insertExecuteController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建执行单信息controller层实现
    @:date 2023/4/5
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def insertExecute(key=1):
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
            # 读取新建的执行单信息
            modeKey = dataDict['modeKey']
            departId = dataDict['departId']
            patientId = dataDict['patientId']
            visitId = dataDict['visitId']
            # modekey=1时，代表新建子单，此时executeItem无效
            executeItem = dataDict['executeItem']
            # modeKey=0时，代表新建执行单，此时executeId无效
            executeId = dataDict['executeId']
            executeSubItem = dataDict['executeSubItem']
            executeLabel = dataDict['executeLabel']
            typeCode = dataDict['typeCode']
            typeLabel = dataDict['typeLabel']
            createStaffId = staff.getStaffId()
            # 创建执行单对象并装载信息
            execute = Execute.Execute()
            execute.setDepartId(departId)
            execute.setPatientId(patientId)
            execute.setVisitId(visitId)
            execute.setExecuteItem(executeItem)
            execute.setExecuteSubItem(executeSubItem)
            execute.setExecuteId(executeId)
            execute.setExecuteLabel(executeLabel)
            execute.setTypeCode(typeCode)
            execute.setTypeLabel(typeLabel)
            execute.setStaffId(createStaffId)
            # 调用sever层
            departExecute = DepartExecute.DepartExecute()
            departExecute.setStaff(staff)
            departExecute.setDepartId(departId)
            departExecute.setExecuteList(execute)
            insertExecuteSever = InsertExecuteSever.InsertExecuteSever()
            # 出参
            respond = insertExecuteSever.insertExecuteSever(departExecute,modeKey)
            if (respond == True):
                retMess = "执行单新建成功"
            else:
                retMess = "执行单新建异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertExecuteController().fullPath #固定部分，不要删除