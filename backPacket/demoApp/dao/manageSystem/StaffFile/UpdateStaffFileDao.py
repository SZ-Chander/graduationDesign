from backPacket.demoApp.dto.manageSystem import StaffFile
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateStaffFileDao
描述：更新护士档案功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/22
备注：
"""
class UpdateStaffFileDao:
    def __init__(self):
        self.staffFileTable = "View_Staff_File"
        self.sysUserTable="sys_user"
        self.db = current_app.config['db']

    """
    功能阐述: 更新护士档案一览功能Dao层主入口
    @:date 2023/4/22
    @:author 马梓洋
    """
    def updateStaffFileDao(self,updateStaffFileS2D):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where userId=:userId ".format(
            self.staffFileTable,updateStaffFileS2D.getSqlValues())
        retData = self.db.engine.execute(text(sqlStr), updateStaffFileS2D.getDaoDict())
        return retData.rowcount

    def updateSysUserDao(self,updateStaffFileS2D2):
        # 读取科室执行单列表
        sqlStr = "update {} SET {} where userId=:userId ".format(
            self.staffFileTable,updateStaffFileS2D2.getSqlValues2())
        retData = self.db.engine.execute(text(sqlStr), updateStaffFileS2D2.getDaoDict2())
        return retData.rowcount