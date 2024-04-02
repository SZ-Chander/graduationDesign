from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateExecuteDao
描述：查询执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/4
备注：
"""
class UpdateExecuteDao:
    def __init__(self):
        self.executeTable = "Table_Execute"
        self.db = current_app.config['db']

    """
    功能阐述: 更新执行单功能Dao层主入口
    @:date 2023/4/4
    @:author 常舜志
    """
    def updateExecuteDao(self,updateExecuteS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where patientId=:patientId and visitId=:visitId and executeId=:executeId and executeSubId=:executeSubId".format(
            self.executeTable,updateExecuteS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateExecuteS2D.getDaoDict())
        return retData.rowcount