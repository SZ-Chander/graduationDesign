from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateRecordAuditDao
描述：审核护理记录功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
备注：
"""
class UpdateRecordAuditDao:
    def __init__(self):
        self.nursingRecordTable = "Table_NursingRecord"
        self.db = current_app.config['db']

    """
    功能阐述: 审核护理记录功能Dao层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateRecordAuditDao(self,updateRecordAuditS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where recordId=:recordId ".format(
            self.nursingRecordTable,updateRecordAuditS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateRecordAuditS2D.getDaoDict())
        return retData.rowcount