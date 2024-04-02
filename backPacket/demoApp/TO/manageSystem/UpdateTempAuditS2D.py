class UpdateTempAuditS2D:
    def __init__(self):

        self.updateKey = None

        self.TempTableId = None

        self.audit=None
        self.auditWhy=None
    def setUpdateTempAudit(self,audit,auditWhy,updateKey):
        self.audit=audit
        self.auditWhy=auditWhy
        self.updateKey=updateKey
    def setTempAuditBaseValues(self,TempTableId):

        self.TempTableId = TempTableId


    def getDaoDict(self):
        daoDict = {"TempTableId":self.TempTableId}
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