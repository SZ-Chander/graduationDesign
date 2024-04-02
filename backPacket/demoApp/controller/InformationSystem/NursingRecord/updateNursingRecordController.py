from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartNursing,NursingRecord
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.InformationSystem.NursingRecord import UpdateNursingRecordSever
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever

routeKey = 'updateNursingRecord'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateNursingRecordController
父类：baseController
描述：更新护理记录功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/8
"""

class updateNursingRecordController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:更新护理记录信息controller层实现
    @:date 2023/4/8
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def updateNursingRecord(key=1):
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
            staffName=staff.getStaffName()
            #

            # 读取护理记录更新信息
            record = NursingRecord.NursingRecord()
            #nursingDate,nursingWhat,inAndOut,selfCareAssess,nursingRounds
            record.setNursingWhat(dataDict['nursingWhat'])
            record.setNursingDate(dataDict['nursingDate'])
            record.setInwater(dataDict['Inwater'])
            record.setSelfCareAssess(dataDict['selfCareAssess'])
            record.setNursingRounds(dataDict['nursingRounds'])
            record.setOutwater(dataDict['Outwater'])
            record.setRecordId(dataDict['recordId'])

            # 信息读取完毕，将工作人员信息和护理记录更新信息打包
            departNursing = DepartNursing.DepartNursing()
            departNursing.setNursingList(record)#虽然变量名是list，但这里实际上不是list，而只是一个实例化对象
            departNursing.setStaff(staff)
            departNursing.setDepartId(dataDict['departId'])
            # 打包完成
            updateRecordSever = UpdateNursingRecordSever.UpdateNursingRecordSever()
            respond = updateRecordSever.updateNursingRecordSever(departNursing)
            if(respond == True):
                retMess = "护理记录修改成功"
            else:
                retMess = "护理记录修改异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateNursingRecordController().fullPath #固定部分，不要删除