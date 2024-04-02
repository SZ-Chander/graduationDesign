from backPacket.demoApp.dto import NursingPlan
from flask import current_app
from sqlalchemy import text
"""
类名：InsertNursingPlanDao
描述：新增护理计划功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
备注：
"""
class InsertNursingPlanDao:
    def __init__(self):
        self.nursingPlanMessTable = "Table_NursingPlan"
        self.db = current_app.config['db']

    """
    功能阐述: 新增护理计划功能Dao层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def insertNursingPlanDao(self,insertNursingPlanS2D):
        # 读取科室执行单列表
        sqlStr = "insert into {} ({}) values ({})".format(self.nursingPlanMessTable,insertNursingPlanS2D.getSqlFormatStr(),insertNursingPlanS2D.getSqlValuesStr())
        # retData = self.db.engine.execute(sqlStr)
        retData = self.db.engine.execute(text(sqlStr), insertNursingPlanS2D.__dict__)
        return retData.rowcount