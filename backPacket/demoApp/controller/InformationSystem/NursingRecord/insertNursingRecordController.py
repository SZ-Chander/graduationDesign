from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartNursing,NursingRecord,NursingAssess
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.InformationSystem.NursingRecord import InsertNursingRecordSever
from backPacket.demoApp.sever.InformationSystem.NursingAssess import InsertNursingAssessSever
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever

routeKey = 'insertNursingRecord'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertNursingRecordController
父类：baseController
描述：新增护理记录功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""

class insertNursingRecordController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建护理记录controller层实现
    @:date 2023/4/19
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def insertNursingRecord(key=1):
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
            # 读取新建的护理记录信息
            departId = dataDict['departId']
            patientId = dataDict['patientId']
            nursingDate = dataDict['nursingDate']
            nursingWhat =dataDict['nursingWhat']
            Inwater=dataDict['Inwater']
            selfCareAssess=dataDict['selfCareAssess']
            nursingRounds=dataDict['nursingRounds']
            Outwater=dataDict['Outwater']
            # 创建护理记录对象并装载信息
            record = NursingRecord.NursingRecord()
            assess=NursingAssess.NursingAssess()
            record.setDepartId(departId)
            record.setPatientId(patientId)
            record.setNursingDate(nursingDate)
            record.setUserId(userId)
            record.setNursingWhat(nursingWhat)
            record.setInwater(Inwater)
            record.setOutwater(Outwater)
            record.setSelfCareAssess(selfCareAssess)
            record.setNursingRounds(nursingRounds)
            assess.setPatientId(patientId)
            # 调用sever层
            departNursingRecord = DepartNursing.DepartNursing()
            departNursingRecord.setStaff(staff)
            departNursingRecord.setDepartId(departId)
            departNursingRecord.setNursingList(record)
            insertNursingRecordSever = InsertNursingRecordSever.InsertNursingRecordSever()
            insertNursingAssessSever= InsertNursingAssessSever.InsertNursingAssessSever()
            # 出参
            respond = insertNursingRecordSever.insertNursingRecordSever(departNursingRecord)#新增护理记录
            respond2=insertNursingAssessSever.insertNursingAssessSever(departNursingRecord)#新增护理评估
            if (respond & respond2 == True):
                retMess = "护理记录新建成功"
            else:
                retMess = "护理记录新建异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertNursingRecordController().fullPath #固定部分，不要删除