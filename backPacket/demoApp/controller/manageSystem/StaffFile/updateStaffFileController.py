from flask import Blueprint, request
from backPacket.demoApp.controller.manageSystem.manageBaseController import manageBaseController
from backPacket.demoApp.dto import Staff,DepartNursing
from backPacket.demoApp.dto.manageSystem import StaffFile
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.manageSystem.StaffFile import UpdateStaffFileSever

routeKey = 'updateStaffFile'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateStaffFileController
父类：manageBaseController
描述：更新护士档案功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/22
"""

class updateStaffFileController(manageBaseController):
    def __init__(self):
        self.basePath = manageBaseController().manageBasePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:更新护士档案信息controller层实现
    @:date 2023/4/22
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def updateStaffFile(key=1):
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

            # 读取护士档案更新信息
            file = StaffFile.StaffFile()
            # userId,name,userDepartCode,departName,autority,sex,birthDate,IDnumber,
            # address,professional,education,employDate,politics

            file.setName(dataDict['name'])

            file.setSex(dataDict['sex'])
            file.setBirthDate(dataDict['birthDate'])
            file.setIDnumber(dataDict['IDnumber'])
            file.setAddress(dataDict['address'])
            file.setProfessional(dataDict['professional'])
            file.setEducation(dataDict['education'])
            file.setEmployDate(dataDict['employDate'])
            file.setPolitics(dataDict['politics'])

            file.setUserId(dataDict['userId'])

            # 信息读取完毕，将工作人员信息和护士档案更新信息打包
            departNursing = DepartNursing.DepartNursing()
            departNursing.setNursingList(file)#虽然变量名是list，但这里实际上不是list，而只是一个实例化对象
            departNursing.setStaff(staff)
            departNursing.setDepartId(dataDict['departId'])
            # 打包完成
            updateRecordSever = UpdateStaffFileSever.UpdateStaffFileSever()
            respond = updateRecordSever.updateStaffFileSever(departNursing)
            if(respond == True):
                retMess = "护士档案修改成功"
            else:
                retMess = "护士档案修改异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateStaffFileController().fullPath #固定部分，不要删除