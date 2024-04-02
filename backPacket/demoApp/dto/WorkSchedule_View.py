class WorkSchedule_View:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.editTime = None
        self.createStaffName = None
        self.workStaffId = None
        self.workStaffName = None
        self.workDepartName = None
        self.workId = None

    def setEditTime(self,editTime):
        self.editTime = editTime
    def setStartTime(self,startTime:str):
        self.startTime = startTime
    def setEndTime(self,endTime:str):
        self.endTime = endTime
    def setCreateStaffName(self,createStaffName:str):
        self.createStaffName = createStaffName
    def setWorkStaffName(self,workStaffName:str):
        self.workStaffName = workStaffName
    def setWorkDepartName(self,workDepartName:str):
        self.workDepartName = workDepartName
    def setWorkId(self,workId:str):
        self.workId = workId
    def setWorkStaffId(self,workStaffId:str):
        self.workStaffId = workStaffId

    def getEditTime(self):
        return self.editTime
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def getCreateStaffName(self):
        return self.createStaffName
    def getWorkStaffName(self):
        return self.workStaffName
    def getWorkDepartName(self):
        return self.workDepartName
    def getWorkId(self):
        return self.workId
    def getWorkStaffId(self):
        return self.workStaffId