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
class InsertWorkScheduleDao:
    def __init__(self):
        self.procedure = "insertWorkSchedule"
        self.db = current_app.config['db']

    """
    功能阐述: 新建排班信息功能Dao层主入口
    @:date 2023/4/27
    @:author 常舜志
    """
    def insertWorkSchedule(self,workSchedule):
        try:
            startTime = workSchedule.getStartTime()
            endTime = workSchedule.getEndTime()
            createStaffId = workSchedule.getCreateStaffId()
            workStaffId = workSchedule.getWorkStaffId()
            workStaffDepart = workSchedule.getWorkStaffDepart()
            sqlStrProcedure = 'CALL {}(:startTime,:endTime,:createStaffId,:workStaffId,:workStaffDepart,@out_statusCode)'.format(self.procedure)
            dataDict = dict(startTime=startTime,endTime=endTime,createStaffId=createStaffId,workStaffId=workStaffId,workStaffDepart=workStaffDepart)
            sqlSelect = "select @out_statusCode"
            self.db.session.execute(text(sqlStrProcedure),dataDict)
            retMess = list(self.db.session.execute(sqlSelect))
            self.db.session.commit()
            self.db.session.close()
            retData = retMess[0][0]
        except Exception as e:
            print("Error as {}".format(e))
            retData = -1
        return retData