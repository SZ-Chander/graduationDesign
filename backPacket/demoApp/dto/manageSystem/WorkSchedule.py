from ..Staff import Staff

class WorkSchedule:
    def __init__(self):
        self.startTime = None
        self.endTime = None
        self.createTime = None
        self.createStaffId = None
        self.editTime = None
        self.workStaffId = None
        self.workStaffDepart = None
        self.workId = None
        self.staff = None
        self.departId = None

    def setStaff(self,staff:Staff):
        self.staff = staff
    def setDepartId(self,departId:str):
        self.departId = departId
    def setStartTime(self,startTime:str):
        self.startTime = startTime
    def setEndTime(self,endTime:str):
        self.endTime = endTime
    def setCreateTime(self,createTime:str):
        self.createTime = createTime
    def setCreateStaffId(self,createStaffId:str):
        self.createStaffId = createStaffId
    def setEditTime(self,editTime:str):
        self.editTime = editTime
    def setWorkStaffId(self,workStaffId:str):
        self.workStaffId = workStaffId
    def setWorkStaffDepart(self,workStaffDepart:str):
        self.workStaffDepart = workStaffDepart
    def setWorkId(self,workId:str):
        self.workId = workId

    def getStaff(self):
        return self.staff
    def getDepartId(self):
        return self.departId
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    def getCreateTime(self):
        return self.createTime
    def getCreateStaffId(self):
        return self.createStaffId
    def getEditTime(self):
        return self.editTime
    def getWorkStaffId(self):
        return self.workStaffId
    def getWorkStaffDepart(self):
        return self.workStaffDepart
    def getWorkId(self):
        return self.workId
