from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateNursingRecordDao
描述：查询护理记录功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/8
备注：
"""
class UpdateNursingRecordDao:
    def __init__(self):
        self.nursingRecordTable = "Table_NursingRecord"
        self.db = current_app.config['db']

    """
    功能阐述: 更新护理记录功能Dao层主入口
    @:date 2023/4/8
    @:author 马梓洋
    """
    def updateNursingRecordDao(self,updateNursingRecordS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where recordId=:recordId ".format(
            self.nursingRecordTable,updateNursingRecordS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateNursingRecordS2D.getDaoDict())
        return retData.rowcount