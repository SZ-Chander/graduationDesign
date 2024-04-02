class UpdatePlanAuditS2D:
    def __init__(self):

        self.updateKey = None

        self.planId = None

        self.audit=None
        self.auditWhy=None
    def setUpdatePlanAudit(self,audit,auditWhy,updateKey):
        self.audit=audit
        self.auditWhy=auditWhy
        self.updateKey=updateKey
    def setPlanAuditBaseValues(self,planId):

        self.planId = planId


    def getDaoDict(self):
        daoDict = {"planId":self.planId}
        if(self.updateKey == 1):
            daoDict["audit"] = 1
            daoDict["auditWhy"]=self.auditWhy
        elif(self.updateKey == 2):
            daoDict["audit"] = 2
            daoDict["auditWhy"]=self.auditWhy
        return daoDict

    def getSqlValues(self):
        if (self.updateKey == 1):
            return "audit=:audit,auditWhy=:auditWhy"
        elif (self.updateKey == 2):
            return "audit=:audit,auditWhy=:auditWhy"