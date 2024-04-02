from ..dto.Staff import Staff
class UnwellLogPage:
    def __init__(self):
        self.unwellLogList = None
        self.staff = None
        self.departId = None
        self.departName = None

    def setUnwellLogList(self,unwellLogList):
        self.unwellLogList = unwellLogList
    def setStaff(self,staff:Staff):
        self.staff = staff
    def setDepartId(self,departId:str):
        self.departId = departId
    def setDepartName(self,departName:str):
        self.departName = departName

    def getUnwellLogList(self):
        return self.unwellLogList
    def getStaff(self):
        return self.staff
    def getDepartId(self):
        return self.departId
    def getDepartName(self):
        return self.departName

    def setStartTime(self,startTime):
        self.startTime = startTime
    def setEndTime(self,endTime):
        self.endTime = endTime
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
