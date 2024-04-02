from backPacket.demoApp.dto import NursingAssess
from flask import current_app
from sqlalchemy import text
"""
类名：NursingAssessDao
描述：护理评估Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/30
备注：
"""
class NursingAssessDao:
    def __init__(self):
        self.nursingAssessTable = "View_inNursingAssess"
        self.db = current_app.config['db']

    """
    功能阐述: 护理评估Dao层主入口
    @:date 2023/4/30
    @:author 马梓洋
    """
    def nursingAssessDao(self,depart):
        sqlStr = "select * from {} where departId=:departId and createDate BETWEEN :BeginDate AND :EndDate".format(self.nursingAssessTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId(),BeginDate=depart.getBeginDate(),EndDate=depart.getEndDate())))

        AssessList = []
        for nursingAssess in retData:
            assess = NursingAssess.NursingAssess()
            assess.setNursingAssess1(
                patientName1=nursingAssess[0],patientAge=nursingAssess[1],recordId=nursingAssess[2],departId=nursingAssess[3],departName=nursingAssess[4],
                createDate=nursingAssess[5],lastUpDate=nursingAssess[6],name=nursingAssess[7],nursingAssess=nursingAssess[8],allergy=nursingAssess[9],
                conscious=nursingAssess[10],position=nursingAssess[11],communication=nursingAssess[12],limb=nursingAssess[13],
                swallow=nursingAssess[14],eyes=nursingAssess[15],food=nursingAssess[16],shit=nursingAssess[17],pee=nursingAssess[18],
                chronic=nursingAssess[19],audit=nursingAssess[20],auditWhy=nursingAssess[21],patientId=nursingAssess[22]
            )
            AssessList.append(assess)
        depart.setNursingList(AssessList)
        return depart