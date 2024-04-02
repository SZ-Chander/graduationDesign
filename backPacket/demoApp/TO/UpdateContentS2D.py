class UpdateContentTOS2D:
    def __init__(self):
        self.sqlStr = None
        self.valueDict = None
        self.daoFuntionKey = None

    def setSqlStr(self,sqlStr:str):
        self.sqlStr = sqlStr
    def setValueDict(self,valueDict:dict):
        self.valueDict = valueDict
    def setDaoFuntionKey(self,daoFuntionKey):
        self.daoFuntionKey = daoFuntionKey

    def getSqlStr(self):
        return self.sqlStr
    def getValueDict(self):
        return self.valueDict
    def getDaoFuntionKey(self):
        return self.daoFuntionKey