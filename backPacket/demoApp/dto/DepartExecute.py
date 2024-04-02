class DepartExecute:
    def __init__(self):
        self.executeList = None
        self.staff = None
        self.departId = None
        self.departName = None
    def setDepart(self,departExecuteList,staff):
        self.departExecuteList = departExecuteList
        self.staff = staff
    def setStaff(self,staff):
        self.staff = staff
    def setExecuteList(self,executeList):
        self.executeList = executeList
    def getDepartId(self):
        return self.departId
    def setDepartName(self,departName):
        self.departName = departName
    def setDepartId(self,departId):
        self.departId = departId
    def getStaff(self):
        return self.staff
    def getExecuteList(self):
        return self.executeList
    def setStartTime(self,startTime):
        self.startTime = startTime
    def setEndTime(self,endTime):
        self.endTime = endTime
    def getStartTime(self):
        return self.startTime
    def getEndTime(self):
        return self.endTime
    """
    功能阐述:快速将全dto完全字典化的快速方法
    @:date 2023/03/28
    @:author 常舜志
    """
    def obj2Dict(self):
        self.staff = self.staff.__dict__
        executeMess = []
        for execute in self.executeList:
            executeMess.append(execute.__dict__)
        self.executeList = executeMess