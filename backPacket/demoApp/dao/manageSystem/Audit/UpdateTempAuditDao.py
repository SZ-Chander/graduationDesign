from backPacket.demoApp.dto import NursingPlan
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateTempAuditDao
描述：审核体温单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
备注：
"""
class UpdateTempAuditDao:
    def __init__(self):
        self.nursingTempTable = "Table_Temperature"
        self.db = current_app.config['db']

    """
    功能阐述: 审核体温单功能Dao层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateTempAuditDao(self,updateTempAuditS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where TempTableId=:TempTableId ".format(
            self.nursingTempTable,updateTempAuditS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateTempAuditS2D.getDaoDict())
        return retData.rowcount