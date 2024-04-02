from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateAssessAuditDao
描述：审核护理评估功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
备注：
"""
class UpdateAssessAuditDao:
    def __init__(self):
        self.nursingAssessTable = "Table_NursingAssess"
        self.db = current_app.config['db']

    """
    功能阐述: 审核护理评估功能Dao层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateAssessAuditDao(self,updateAssessAuditS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where recordId=:recordId ".format(
            self.nursingAssessTable,updateAssessAuditS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateAssessAuditS2D.getDaoDict())
        return retData.rowcount