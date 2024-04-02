from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateNursingAssessDao
描述：查询护理评估功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
备注：
"""
class UpdateNursingAssessDao:
    def __init__(self):
        self.nursingAssessTable = "Table_NursingAssess"
        self.db = current_app.config['db']

    """
    功能阐述: 更新护理评估功能Dao层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def updateNursingAssessDao(self,updateNursingAssessS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where recordId=:recordId".format(
            self.nursingAssessTable,updateNursingAssessS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateNursingAssessS2D.getDaoDict())
        return retData.rowcount