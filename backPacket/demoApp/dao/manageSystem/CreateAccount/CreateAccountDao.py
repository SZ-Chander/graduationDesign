from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：CreatAccountDao
描述：新建执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
备注：
"""
class CreateAccountDao:
    def __init__(self):
        self.procedure = "CreateNewAccount"
        self.db = current_app.config['db']

    """
    功能阐述: 创建新用户功能Dao层主入口
    @:date 2023/4/5
    @:author 常舜志
    """
    def creatAccountDao(self,staff):
        try:
            sqlStr = 'CALL {}("{}","{}","{}",{})'.format(self.procedure,staff.getStaffName(),staff.getStaffId(),staff.getDepartCode(),staff.getStaffAutority())
            self.db.session.execute(sqlStr)
            self.db.session.commit()
            self.db.session.close()
            retData  = 1
        except Exception as e:
            retData = -1
        return retData