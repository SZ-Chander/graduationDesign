from flask import Blueprint, request
from backPacket.demoApp.controller.manageSystem.manageBaseController import manageBaseController
from backPacket.demoApp.dto import Staff,DepartNursing
from backPacket.demoApp.dto.manageSystem import StaffFile
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.manageSystem.StaffFile import InsertStaffFileSever

routeKey = 'insertStaffFile'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertStaffFileController
父类：baseController
描述：新增护士档案功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/23
"""

class insertStaffFileController(manageBaseController):
    def __init__(self):
        self.basePath = manageBaseController().manageBasePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建护士档案controller层实现
    @:date 2023/4/23
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def insertStaffFile(key=1):
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
            # userId,sex,birthDate,IDnumber,
            # address,professional,education,employDate,politics
            userId2 = dataDict['userId']
            sex = dataDict['sex']
            birthDate = dataDict['birthDate']
            IDnumber =dataDict['IDnumber']
            address=dataDict['address']
            professional=dataDict['professional']
            education=dataDict['education']
            employDate=dataDict['employDate']
            politics=dataDict['politics']
            departId=dataDict['departId']
            # 创建护理记录对象并装载信息
            record = StaffFile.StaffFile()
            record.setUserId(userId2)
            record.setSex(sex)
            record.setBirthDate(birthDate)
            record.setIDnumber(IDnumber)
            record.setAddress(address)
            record.setProfessional(professional)
            record.setEducation(education)
            record.setEmployDate(employDate)
            record.setPolitics(politics)
            # 调用sever层
            depart = DepartNursing.DepartNursing()
            depart.setStaff(staff)
            depart.setDepartId(departId)
            depart.setNursingList(record)
            insertStaffFileSever = InsertStaffFileSever.InsertStaffFileSever()
            # 出参
            respond = insertStaffFileSever.insertStaffFileSever(depart)
            if (respond == True):
                retMess = "护士档案新建成功"
            else:
                retMess = "护士档案新建异常，code:Error30{}".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertStaffFileController().fullPath #固定部分，不要删除