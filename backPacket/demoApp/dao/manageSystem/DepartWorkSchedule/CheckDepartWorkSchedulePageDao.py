from backPacket.demoApp.dto.WorkSchedule_View import WorkSchedule_View
from backPacket.demoApp.dto.WorkSchedulePage import WorkSchedulePage
from backPacket.demoApp.tools.usefulTools import UsefulTools
from flask import current_app
from sqlalchemy import text
"""
类名：CheckDepartWorkSchedulePageDao
描述：新建执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
备注：
"""
class CheckDepartWorkSchedulePageDao:
    def __init__(self):
        self.dataTable = "View_WorkSchedule"
        self.db = current_app.config['db']

    """
    功能阐述: 创建新用户功能Dao层主入口
    @:date 2023/4/5
    @:author 常舜志
    """
    def CheckDepartWorkSchedulePage(self,workSchedule):
        try:
            sqlStr = "select startTime,endTime,editTime,creatStaffName,workStaffName,workDepartName,workId,workStaffId from {} where workStaffDepartId=:workStaffDepartId and startTime BETWEEN :startTime and :endTime".format(self.dataTable)
            startTime = "{}".format(workSchedule.getStartTime())
            endTime = "{}".format(workSchedule.getEndTime())
            dataDict = dict(workStaffDepartId=workSchedule.getDepartId(),startTime=startTime,endTime=endTime)
            retData = list(self.db.engine.execute(text(sqlStr),dataDict))
            usefulTools = UsefulTools()
            formatString = "%Y年%m月%d日 %H:%M:%S"
            dataList = []
            for dateLine in retData:
                workSchedule_View = WorkSchedule_View()
                workSchedule_View.setStartTime(usefulTools.dateTime2String(dateLine[0],formatString))
                workSchedule_View.setEndTime(usefulTools.dateTime2String(dateLine[1],formatString))
                workSchedule_View.setEditTime(usefulTools.dateTime2String(dateLine[2],formatString))
                workSchedule_View.setCreateStaffName(dateLine[3])
                workSchedule_View.setWorkStaffName(dateLine[4])
                workSchedule_View.setWorkDepartName(dateLine[5])
                workSchedule_View.setWorkId(dateLine[6])
                workSchedule_View.setWorkStaffId(dateLine[7])
                dataList.append(workSchedule_View)
            workSchedulePage = WorkSchedulePage()
            workSchedulePage.setWorkScheduleList(dataList)
            retData = workSchedulePage
        except Exception as e:
            print("Error as {}".format(e))
            retData = e
        finally:
            return retData
