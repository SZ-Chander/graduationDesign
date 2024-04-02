from backPacket.demoApp.dao.InformationSystem.NursingPlan import InsertNursingPlanDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import InsertNursingPlanS2D

"""
类名：insertNursingPlanSever
描述：新增护理计划Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class InsertNursingPlanSever:

    """
    功能阐述:新建护理计划功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def insertNursingPlanSever(self,departNursingPlan):
        try:
            dateStringFormat = "%Y-%m-%d %H:%M:%S"
            dateStringFormat2="%Y%m%d%H%M%S"
            departId = departNursingPlan.getDepartId()
            staff = departNursingPlan.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingPlan.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                nursingPlan = departNursingPlan.getNursingList()
                createDate = usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat)
                planId="P"+nursingPlan.getpatientId()+usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat2)
                lastUpdateDate=createDate
                dischargeKey=0
                planStatus=0
                audit=0
                # 装载参数进入TO
                insertNursingPlanS2D = InsertNursingPlanS2D.InsertNursingPlanS2D()
                insertNursingPlanS2D.setInsertNursingPlanBaseMess(
                    planId=planId,patientId=nursingPlan.getpatientId(),visitId=nursingPlan.getvisitId(),
                    dischargeKey=dischargeKey,planStatus=planStatus,nursingPlan=nursingPlan.getnursingPlan(),
                    planEmergency=nursingPlan.getplanEmergency(),patientStatus=nursingPlan.getpatientStatus(),lastUpdateDate=lastUpdateDate,
                    createDate=createDate,planUserId=nursingPlan.getplanUserId(),audit=audit)
                # 调用dao层
                insertNursingPlanDao = InsertNursingPlanDao.InsertNursingPlanDao()
                rowCount = insertNursingPlanDao.insertNursingPlanDao(insertNursingPlanS2D)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def setDepartName(self,depart):
        departMessList = depart.getStaff().getDepart()
        departId = depart.getDepartId()
        for departMess in departMessList:
            if(departId == departMess[0]):
                depart.setDepartName(departMess[1])
                break