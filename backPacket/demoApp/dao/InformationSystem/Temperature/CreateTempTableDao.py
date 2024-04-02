from backPacket.demoApp.dto import TempTable
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateTemperatureDao
描述：创建体温单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/18
备注：
"""
class CreateTempTableDao:
    def __init__(self):
        self.TemperatureTable = "Table_Temperature"
        self.TempTable="View_TempTable"
        self.db = current_app.config['db']

    """
    功能阐述: 创建体温单功能Dao层主入口
    @:date 2023/4/18
    @:author 马梓洋
    """
    def createTempTableDao(self,CreateTempTableS2D):
        # 读取科室执行单列表
        for a in CreateTempTableS2D.getTempIdList():
            sqlStr = "update {} SET {} where TempId=:TempId".format(
                self.TemperatureTable,CreateTempTableS2D.getSqlValues())
            retData = (self.db.engine.execute(text(sqlStr), dict(TempId=a,TempTableId=CreateTempTableS2D.getTempTableId())))
            #retData = self.db.engine.execute(text(sqlStr), CreateTempTableS2D.getDaoDict())
        return retData.rowcount