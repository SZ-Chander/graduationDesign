from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartNursing,Temperature
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.InformationSystem.Temperature import InsertTemperatureSever
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever

routeKey = 'insertTemperature'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertTemperatureController
父类：baseController
描述：新增体温信息功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/20
"""

class insertTemperatureController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建体温信息controller层实现
    @:date 2023/4/20
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def insertTemperature(key=1):
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
            # 读取新建的体温单信息
            # patientId,createDate,userId,testDate,temperature,
            # pulse,breathe,shit,inWater,pee,weight,bloodPressure
            departId = dataDict['departId']
            patientId = dataDict['patientId']
            testDate = dataDict['testDate']
            temperature2 =dataDict['temperature']
            pulse=dataDict['pulse']
            breathe=dataDict['breathe']
            shit=dataDict['shit']
            inWater=dataDict['inWater']
            pee=dataDict['pee']
            weight=dataDict['weight']
            bloodPressure=dataDict['bloodPressure']

            # 创建体温单对象并装载信息
            temperature = Temperature.Temperature()
            temperature.setDepartId(departId)
            temperature.setPatientId(patientId)
            temperature.setTestDate(testDate)
            temperature.setUserId(userId)
            temperature.setTemperature2(temperature2)
            temperature.setPulse(pulse)
            temperature.setBreathe(breathe)
            temperature.setShit(shit)
            temperature.setInWater(inWater)
            temperature.setPee(pee)
            temperature.setWeight(weight)
            temperature.setBloodPressure(bloodPressure)

            # 调用sever层
            departTemperature = DepartNursing.DepartNursing()
            departTemperature.setStaff(staff)
            departTemperature.setDepartId(departId)
            departTemperature.setNursingList(temperature)
            insertTemperatureSever = InsertTemperatureSever.InsertTemperatureSever()
            # 出参
            respond = insertTemperatureSever.insertTemperatureSever(departTemperature)
            if (respond == True):
                retMess = "体温信息录入成功"
            else:
                retMess = "体温信息录入异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertTemperatureController().fullPath #固定部分，不要删除