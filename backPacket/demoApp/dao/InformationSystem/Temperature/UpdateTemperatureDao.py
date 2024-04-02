from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateTemperatureDao
描述：更新体温信息功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/18
备注：
"""
class UpdateTemperatureDao:
    def __init__(self):
        self.TemperatureTable = "Table_Temperature"
        self.db = current_app.config['db']

    """
    功能阐述: 更新体温信息功能Dao层主入口
    @:date 2023/4/18
    @:author 马梓洋
    """
    def updateTemperatureDao(self,updateTemperatureS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where patientId=:patientId and TempId=:TempId".format(
            self.TemperatureTable,updateTemperatureS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateTemperatureS2D.getDaoDict())
        return retData.rowcount