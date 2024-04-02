class UpdateAssessAuditS2D:
    def __init__(self):

        self.updateKey = None

        self.recordId = None

        self.audit_A=None
        self.auditWhy_A=None
    def setUpdateAssessAudit(self,audit_A,auditWhy_A,updateKey):
        self.audit_A=audit_A
        self.auditWhy_A=auditWhy_A
        self.updateKey=updateKey
    def setAssessAuditBaseValues(self,recordId):

        self.recordId = recordId


    def getDaoDict(self):
        daoDict = {"recordId":self.recordId}
        if(self.updateKey == 1):
            daoDict["audit"] = 1
            daoDict["auditWhy"]=self.auditWhy_A
        elif(self.updateKey == 2):
            daoDict["audit"] = 2
            daoDict["auditWhy"]=self.auditWhy_A
        return daoDict

    def getSqlValues(self):
        if (self.updateKey == 1):
            return "audit=:audit,auditWhy=:auditWhy"
        elif (self.updateKey == 2):
            return "audit=:audit,auditWhy=:auditWhy"