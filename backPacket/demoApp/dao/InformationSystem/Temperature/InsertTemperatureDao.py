from backPacket.demoApp.dto import Temperature
from flask import current_app
from sqlalchemy import text
"""
类名：InsertNursingTemperatureDao
描述：新增体温信息功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/20
备注：
"""
class InsertTemperatureDao:
    def __init__(self):
        self.temperatureMessTable = "Table_Temperature"
        self.db = current_app.config['db']

    """
    功能阐述: 新增体温信息功能Dao层主入口
    @:date 2023/4/20
    @:author 马梓洋
    """
    def insertTemperatureDao(self,insertTemperatureS2D):
        # 读取科室执行单列表
        sqlStr = "insert into {} ({}) values ({})".format(self.temperatureMessTable,insertTemperatureS2D.getSqlFormatStr(),insertTemperatureS2D.getSqlValuesStr())
        # retData = self.db.engine.execute(sqlStr)
        retData = self.db.engine.execute(text(sqlStr), insertTemperatureS2D.__dict__)
        return retData.rowcount