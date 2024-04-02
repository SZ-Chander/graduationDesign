class UpdateExecuteS2D:
    def __init__(self):
        self.executeTime = None
        self.executeKey = None
        self.completeDate = None
        self.completeKey = None
        self.updateKey = None
        self.sqlValues = None
        self.patientId = None
        self.visitId = None
        self.executeId = None
        self.executeSubId = None
        self.executeLabel =None
    def setUpdateExecute(self,executeTime,executeKey,completeDate,completeKey,updateKey):
        self.executeTime = executeTime
        self.executeKey = executeKey
        self.completeDate = completeDate
        self.completeKey = completeKey
        self.updateKey = updateKey
    def setExecuteBaseValues(self,patientId,visitId,executeId,executeSubId,executeLabel):
        self.patientId = patientId
        self.visitId = visitId
        self.executeId = executeId
        self.executeSubId = executeSubId
        self.executeLabel = executeLabel
    def getDaoDict(self):
        daoDict = {"patientId":self.patientId,"visitId":self.visitId,"executeId":self.executeId,"executeSubId":self.executeSubId,"executeLabel":self.executeLabel}
        if(self.updateKey == 1):
            daoDict["executeTime"] = self.executeTime
            daoDict["executeKey"] = 1
        elif(self.updateKey == 2):
            daoDict["completeDate"] = self.completeDate
            daoDict["completeKey"] = 1
        elif(self.updateKey == 3):
            daoDict["executeTime"] = self.executeTime
            daoDict["executeKey"] = 1
            daoDict["completeDate"] = self.completeDate
            daoDict["completeKey"] = 1
        return daoDict

    def getSqlValues(self):
        if (self.updateKey == 1):
            return "executeTime=:executeTime,executeKey=:executeKey,executeLabel=:executeLabel"
        elif (self.updateKey == 2):
            return "completeDate=:completeDate,completeKey=:completeKey,executeLabel=:executeLabel"
        elif (self.updateKey == 3):
            return "executeTime=:executeTime,executeKey=:executeKey,completeDate=:completeDate,completeKey=:completeKey,executeLabel=:executeLabel"