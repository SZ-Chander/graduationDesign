from backPacket.demoApp.dto.manageSystem import StaffFile
from flask import current_app
from sqlalchemy import text
"""
类名：InsertStaffFileDao
描述：新增护士档案功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/23
备注：
"""
class InsertStaffFileDao:
    def __init__(self):
        self.staffFileMessTable = "Table_StaffFile"
        self.db = current_app.config['db']

    """
    功能阐述: 新增护士档案功能Dao层主入口
    @:date 2023/4/23
    @:author 马梓洋
    """
    def insertStaffFileDao(self,insertStaffFileS2D):
        # 读取科室执行单列表
        sqlStr = "insert into {} ({}) values ({})".format(self.staffFileMessTable,insertStaffFileS2D.getSqlFormatStr(),insertStaffFileS2D.getSqlValuesStr())
        # retData = self.db.engine.execute(sqlStr)
        retData = self.db.engine.execute(text(sqlStr), insertStaffFileS2D.__dict__)
        return retData.rowcount

    def selectUserIdDao(self,select):
        sqlStr ="select * from {} where userId=:userId ".format(self.staffFileMessTable)
        retData = self.db.engine.execute(text(sqlStr),select.getDaoDict())
        return retData.rowcount