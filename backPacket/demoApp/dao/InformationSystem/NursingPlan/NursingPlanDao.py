from backPacket.demoApp.dto import NursingPlan
from flask import current_app
from sqlalchemy import text
"""
类名：NursingPlanDao
描述：护理计划Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/3/30
备注：
"""
class NursingPlanDao:
    def __init__(self):
        self.nursingPlanTable = "View_inNursingPlan"
        self.db = current_app.config['db']

    """
    功能阐述: 护理计划Dao层主入口
    @:date 2023/3/30
    @:author 马梓洋
    """
    def nursingPlanDao(self,depart):

        sqlStr = "select * from {} where departId=:departId and createDate BETWEEN :BeginDate AND :EndDate".format(self.nursingPlanTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId(),BeginDate=depart.getBeginDate(),EndDate=depart.getEndDate())))

        planList = []
        for nursingPlan in retData:
            plan = NursingPlan.NursingPlan()
            plan.setNursingPlan1(
                planId=nursingPlan[0],planStatus=nursingPlan[1],patientDepartId=nursingPlan[2],departName=nursingPlan[3],
                patientName=nursingPlan[4],patientId=nursingPlan[5],nursingPlan=nursingPlan[6],planEmergency=nursingPlan[7],
                patientStatus=nursingPlan[8],lastUpdateDate=nursingPlan[9],createDate=nursingPlan[10],planUser=nursingPlan[11],
                stopDate=nursingPlan[12],stopWhy=nursingPlan[13],stopUser=nursingPlan[14],visitId=nursingPlan[15],
                audit=nursingPlan[16],auditWhy=nursingPlan[17]
            )
            planList.append(plan)
        depart.setNursingList(planList)
        return depart