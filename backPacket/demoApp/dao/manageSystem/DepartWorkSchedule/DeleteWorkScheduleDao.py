from flask import current_app
from sqlalchemy import text
"""
类名：InsertWorkScheduleDao
描述：新建排班信息功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
备注：
"""
class DeleteWorkScheduleDao:
    def __init__(self):
        self.tableName = "Table_WorkSchedule"
        self.db = current_app.config['db']

    """
    功能阐述: 新建排班信息功能Dao层主入口
    @:date 2023/5/23
    @:author 常舜志
    """
    def deleteWorkSchedule(self,workSchedule):
        try:

            workId = workSchedule.getWorkId()
            sqlStr = "DELETE FROM Table_WorkSchedule WHERE workId =:workId"
            dataDict = dict(workId=workId)
            retData = self.db.engine.execute(text(sqlStr),dataDict)
        except Exception as e:
            print("Error as {}".format(e))
            retData = -10
        return retData.rowcount