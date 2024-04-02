class WhiteBoardRoutines:
    def __init__(self):
        self.departId = None
        self.staff = None
        self.bedDict = None
        self.usingBedCount = None
        self.enterPatientCount = None
        self.outPatientCount = None
        self.workingStaffNameStr = None
        self.workingStaffCount = None
    def setWhiteBoardRoutines(self,bedDict,usingBedCount,enterPatientCount,outPatientCount,workingStaffNameStr,workingStaffCount):
        self.bedDict = bedDict
        self.usingBedCount = usingBedCount
        self.enterPatientCount = enterPatientCount
        self.outPatientCount = outPatientCount
        self.workingStaffNameStr = workingStaffNameStr
        self.workingStaffCount = workingStaffCount
    def setStaff(self,staff):
        self.staff = staff
    def setDepartId(self,departId):
        self.departId = departId
    def getDepartId(self):
        return self.departId
    def getStaff(self):
        return self.staff
    def getOutPatientCount(self):
        return self.outPatientCount
    def getEnterPatientCount(self):
        return self.enterPatientCount
    def getWorkingStaffCount(self):
        return self.workingStaffCount
    def getWorkingStaffNameStr(self):
        return self.workingStaffNameStr
    def getBedDict(self):
        return self.bedDict
    def getUsingBedCount(self):
        return self.usingBedCount

    def setStartTime(self,startTime):
        self.startTime = startTime
    def setEndTime(self,endTime):
        self.endTime = endTime
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime