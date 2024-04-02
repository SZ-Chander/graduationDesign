from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartTemperature,TempTable
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.InformationSystem.Temperature import CreateTempTableSever
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever

routeKey = 'createTempTable'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：createTempTableController
父类：baseController
描述：创建体温单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/18
"""

class createTempTableController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:创建体温单controller层实现
    @:date 2023/4/18
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def createTempTable(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的执行单信息
        """
        retMess = 0
        try:
            # 以下这一段基本上可以copy到所有json输入的非login的Controller代码中
            dataDict = {}
            i=0
            for item in request.json:
                dataDict[item] = request.json[item] #将request中的信息读取出来
                i=i+1
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
            record = TempTable.TempTable()
            record.setTimes(i)
            i=0
            x=dataDict['TempId']
            # x= str(y).split(',')
            # if(x[-1]==""):
            #     del x[-1]
            while i< len(x):
                record.setTempIdList(x[i])
                i=i+1

            #信息读取完毕，将工作人员信息和护理记录更新信息打包
            departTemperature = DepartTemperature.DepartTemperature()
            departTemperature.setTemperatureList(record)#虽然变量名是list，但这里实际上不是list，而只是一个实例化对象
            departTemperature.setStaff(staff)
            departTemperature.setDepartId(dataDict['departId'])
            # 打包完成
            createTempTable = CreateTempTableSever.CreateTempTableSever()
            respond = createTempTable.createTempTableSever(departTemperature)
            if(respond == True):
                retMess = "体温单创建成功,包含"+str(i)+"条体温信息\n体温单号为："+str(departTemperature.getTempTableId())
            else:
                retMess = "体温单创建异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = createTempTableController().fullPath #固定部分，不要删除