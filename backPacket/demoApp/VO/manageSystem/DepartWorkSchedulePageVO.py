from ...dto.WorkSchedulePage import WorkSchedulePage
from ...dto.WorkSchedule_View import WorkSchedule_View
from datetime import datetime
from ...tools.usefulTools import UsefulTools

class DepartWorkSchedulePageVO:
    def __init__(self):
        self.workScheduleList = None
        self.staff = None

    def setWorkScheduleList(self,workScheduleList):
        self.workScheduleList = workScheduleList
    def setStaff(self,staff):
        self.staff = staff

    def getStaff(self):
        return self.staff
    def getWorkScheduleList(self):
        return self.workScheduleList

    def setVOfromDTO(self,workSchedulePage:WorkSchedulePage):
        self.staff = workSchedulePage.getStaff().__dict__
        workDataDictList = list(map(self.setScheduleDictFromView,workSchedulePage.getWorkScheduleList()))
        newDataDict = self.workData2DateList(workDataDictList)
        # self.dataList2Dict(newDataDict)
        # self.workScheduleList = newDataDict
        self.workScheduleList = self.dataList2Dict(newDataDict)

    def setScheduleDictFromView(self,workSchedule_View:WorkSchedule_View):
        startTime = workSchedule_View.getStartTime()
        endTime = workSchedule_View.getEndTime()
        editTime = workSchedule_View.getEditTime()
        createStaffName = workSchedule_View.getCreateStaffName()
        workStaffId = workSchedule_View.getWorkStaffId()
        workStaffName = workSchedule_View.getWorkStaffName()
        workDepartName = workSchedule_View.getWorkDepartName()
        workId = workSchedule_View.getWorkId()
        return dict(startTime=startTime,endTime=endTime,editTime=editTime,
                    createStaffName=createStaffName,workStaffId=workStaffId,
                    workStaffName=workStaffName,workDepartName=workDepartName,workId=workId)

    def workData2DateList(self,workDataDictList:list):
        newDataDict = {}
        for workDataDict in workDataDictList:
            startTime = workDataDict['startTime']
            startDateTime = datetime.strptime(startTime,"%Y年%m月%d日 %H:%M:%S")
            startTimeStr = UsefulTools().dateTime2String(startDateTime,"%Y年%m月%d日")
            try:
                newDataDict[startTimeStr].append(workDataDict)
            except:
                newDataDict[startTimeStr] = []
                newDataDict[startTimeStr].append(workDataDict)
        return newDataDict

    def dataList2Dict(self,workDataDict:dict):
        newDataDict = {}
        for key in workDataDict:
            newSubDict = {}
            data = workDataDict[key]
            newSubDict['dateKey'] = key
            newSubDict['data'] = data
            newDataDict[key] = newSubDict
        return newDataDict
