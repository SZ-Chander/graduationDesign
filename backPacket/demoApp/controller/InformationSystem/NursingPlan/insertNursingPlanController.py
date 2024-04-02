from flask import Blueprint, request
import backPacket.demoApp.controller.baseController
from backPacket.demoApp.dto import Staff,DepartNursing,NursingPlan
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.InformationSystem.NursingPlan import InsertNursingPlanSever
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever

routeKey = 'insertNursingPlan'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertNursingPlanController
父类：baseController
描述：新增护理计划功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""

class insertNursingPlanController(backPacket.demoApp.controller.baseController.baseController):
    def __init__(self):
        self.basePath = backPacket.demoApp.controller.baseController.baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建护理计划controller层实现
    @:date 2023/4/19
    @:author 马梓洋
    """
    @api_route.route('/', methods=['POST'])
    def insertNursingPlan(key=1):
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
            # 读取新建的护理计划信息
            # planId,patientId,visitId,dischargeKey,planStatus,
            # nursingPlan,planEmergency,patientStatus,lastUpdateDate,createDate,planUserId
            departId = dataDict['departId']
            patientId = dataDict['patientId']
            visitId = dataDict['visitId']
            nursingPlan =dataDict['nursingPlan']
            planEmergency=dataDict['planEmergency']
            patientStatus=dataDict['patientStatus']

            # 创建护理计划对象并装载信息
            plan = NursingPlan.NursingPlan()
            plan.setDepartId(departId)
            plan.setPatientId(patientId)
            plan.setVisitId(visitId)
            plan.setNursingPlan2(nursingPlan)
            plan.setPlanEmergency(planEmergency)
            plan.setPatientStatus(patientStatus)
            plan.setPlanUserId(userId)

            # 调用sever层
            departNursingPlan = DepartNursing.DepartNursing()
            departNursingPlan.setStaff(staff)
            departNursingPlan.setDepartId(departId)
            departNursingPlan.setNursingList(plan)
            insertNursingPlanSever = InsertNursingPlanSever.InsertNursingPlanSever()
            # 出参
            respond = insertNursingPlanSever.insertNursingPlanSever(departNursingPlan)
            if (respond == True):
                retMess = "护理计划新建成功"
            else:
                retMess = "护理计划新建异常，code:Error30{}\n请联系系统管理员".format(respond)
            # 代码块结束

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertNursingPlanController().fullPath #固定部分，不要删除