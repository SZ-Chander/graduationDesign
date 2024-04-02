from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartExecute,Execute
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.InformationSystem.Execute import UpdateExecuteSever
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'updateExecute'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateExecuteController
父类：baseController
描述：更新执行单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/4
"""

class updateExecuteController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:更新执行单信息controller层实现
    @:date 2023/4/4
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def updateExecute(key=1):
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

            # 读取执行单更新信息（更新执行，完成或同时三种模式）
            usefulTools = UsefulTools()
            execute = Execute.Execute()
            updateKey = dataDict["updateKey"]
            if(updateKey == 1):# 用于更新“已执行”
                execute.setExecuteTime(dataDict['executeTime'])
                execute.setExecuteTime(usefulTools.mandarinDate2Format(execute.getExecuteTime(),"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S"))
                execute.setExecuteKey(dataDict['executeKey'])
            elif(updateKey == 2):# 用于更新“已完成”
                execute.setCompleteDate(dataDict['completeDate'])
                execute.setCompleteDate(usefulTools.mandarinDate2Format(execute.getCompleteDate(),"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S"))
                execute.setCompleteKey(dataDict['completeKey'])
            elif(updateKey == 3):# 用于同时更新“已执行”和“已完成”
                execute.setExecuteTime(dataDict['executeTime'])
                execute.setExecuteKey(dataDict['executeKey'])
                execute.setCompleteDate(dataDict['completeDate'])
                execute.setCompleteKey(dataDict['completeKey'])
                execute.setExecuteTime(usefulTools.mandarinDate2Format(execute.getExecuteTime(),"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S"))
                execute.setCompleteDate(usefulTools.mandarinDate2Format(execute.getCompleteDate(),"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S"))

            else:
                raise ValueError("非法数据，更新代码错误")
            execute.setExecuteLabel(dataDict['executeLabel'])
            execute.setPatientId(dataDict['patientId'])
            execute.setVisitId(dataDict['visitId'])
            execute.setExecuteId(dataDict['executeId'])
            execute.setExecuteSubId(dataDict['executeSubId'])


            # 信息读取完毕，将工作人员信息和执行单更新信息打包
            departExecute = DepartExecute.DepartExecute()
            departExecute.setExecuteList(execute)#虽然变量名是list，但这里实际上不是list，而只是一个实例化对象
            departExecute.setStaff(staff)
            departExecute.setDepartId(dataDict['departId'])
            # 打包完成
            updateExecuteSever = UpdateExecuteSever.UpdateExecuteSever()
            respond = updateExecuteSever.updateExecuteSever(departExecute,updateKey)
            if(respond == True):
                retMess = "执行单修改成功"
            else:
                retMess = "执行单修改异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateExecuteController().fullPath #固定部分，不要删除