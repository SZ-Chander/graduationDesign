from backPacket.demoApp.dto.manageSystem import StaffFile
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateStaffFileDao
描述：删除护士档案功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/23
备注：
"""
class DeleteStaffFileDao:
    def __init__(self):
        self.staffFileTable = "Table_StaffFile"

        self.db = current_app.config['db']

    """
    功能阐述: 删除护士档案一览功能Dao层主入口
    @:date 2023/4/22
    @:author 马梓洋
    """
    def deleteStaffFileDao(self,deleteStaffFileS2D):
        # 读取科室执行单列表

        sqlStr = "delete from {} where userId=:userId ".format(self.staffFileTable)
        retData = self.db.engine.execute(text(sqlStr),deleteStaffFileS2D.getDaoDict())
        return retData.rowcount

    def selectUserIdDao(self,select):
        sqlStr ="select * from {} where userId=:userId ".format(self.staffFileTable)
        retData = self.db.engine.execute(text(sqlStr),select.getDaoDict())
        return retData.rowcount