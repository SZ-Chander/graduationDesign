from backPacket.demoApp.dto import NursingPlan
from flask import current_app
from sqlalchemy import text
"""
类名：UpdatePlanAuditDao
描述：审核护理计划功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/24
备注：
"""
class UpdatePlanAuditDao:
    def __init__(self):
        self.nursingPlanTable = "Table_NursingPlan"
        self.db = current_app.config['db']

    """
    功能阐述: 审核护理计划功能Dao层主入口
    @:date 2023/4/6
    @:author 马梓洋
    """
    def updatePlanAuditDao(self,updatePlanAuditS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where planId=:planId ".format(
            self.nursingPlanTable,updatePlanAuditS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updatePlanAuditS2D.getDaoDict())
        return retData.rowcount