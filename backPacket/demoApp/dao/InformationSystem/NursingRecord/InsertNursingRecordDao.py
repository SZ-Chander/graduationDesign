from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：InsertNursingRecordDao
描述：新增护理记录功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
备注：
"""
class InsertNursingRecordDao:
    def __init__(self):
        self.nursingRecordMessTable = "Table_NursingRecord"
        self.db = current_app.config['db']

    """
    功能阐述: 新增护理记录功能Dao层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def insertNursingRecordDao(self,insertNursingRecordS2D):
        # 读取科室执行单列表
        sqlStr = "insert into {} ({}) values ({})".format(self.nursingRecordMessTable,insertNursingRecordS2D.getSqlFormatStr(),insertNursingRecordS2D.getSqlValuesStr())
        # retData = self.db.engine.execute(sqlStr)
        retData = self.db.engine.execute(text(sqlStr), insertNursingRecordS2D.__dict__)
        return retData.rowcount
