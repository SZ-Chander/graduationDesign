class UpdateNursingPlanS2D:
    def __init__(self):
        self.lastUpdateDate = None
        self.planStatus = None
        self.updateKey = None
        self.sqlValues = None
        self.patientId = None
        self.visitId = None
        self.planId = None
        self.nursingPlan = None
        self.stopUser = None
        self.stopWhy = None
        self.stopDate = None
    def setUpdateNursingPlan(self,lastUpdateDate,planStatus,updateKey,stopDate,stopUser,stopWhy,nursingPlan):

        self.lastUpdateDate = lastUpdateDate
        self.planStatus = planStatus
        self.updateKey = updateKey
        self.stopDate = stopDate
        self.stopUser = stopUser
        self.stopWhy = stopWhy
        self.nursingPlan = nursingPlan
    def setNursingPlanBaseValues(self,planId):

        self.planId = planId


    def getDaoDict(self):
        daoDict = {"planId":self.planId}
        if(self.updateKey == 0):
            daoDict["lastUpdateDate"] = self.lastUpdateDate
            daoDict["nursingPlan"] = self.nursingPlan
        elif(self.updateKey == 1):
            daoDict["lastUpdateDate"] = self.lastUpdateDate
            daoDict["planStatus"] = 1
            daoDict["nursingPlan"] = self.nursingPlan
        elif(self.updateKey == 2):
            daoDict["lastUpdateDate"] = self.lastUpdateDate
            daoDict["stopDate"] = self.stopDate
            daoDict["planStatus"] = 2
            daoDict["stopUser"] = self.stopUser
            daoDict["stopWhy"] = self.stopWhy
            daoDict["nursingPlan"] = self.nursingPlan
        return daoDict

    def getSqlValues(self):
        if (self.updateKey == 0):
            return "lastUpdateDate=:lastUpdateDate,nursingPlan=:nursingPlan"
        if (self.updateKey == 1):
            return "lastUpdateDate=:lastUpdateDate,planStatus=:planStatus,nursingPlan=:nursingPlan"
        elif (self.updateKey == 2):
            return "lastUpdateDate=:lastUpdateDate,planStatus=:planStatus,nursingPlan=:nursingPlan,stopDate=:stopDate,stopUserId=:stopUser,stopWhy=:stopWhy"