class CreateTempTableS2D:
    def __init__(self):
        self.TempTableId = None
        self.TempId=None
        self.TempIdList=None


    def setTempTableId(self,TempTableId):#设置需要更新的字段
        self.TempTableId = TempTableId

    def setTempTableBaseValues(self,TempId):#主键字段
        self.TempId = TempId
    def setTempIdList(self,TempIdList):
        self.TempIdList=TempIdList

    def getTempTableId(self):
        return self.TempTableId
    def getTempIdList(self):
        return self.TempIdList
    def getDaoDict(self):
        daoDict = {"TempId":self.TempId}
        daoDict["TempTableId"] = self.TempTableId
        return daoDict

    def getSqlValues(self):
        return "TempTableId=:TempTableId"
