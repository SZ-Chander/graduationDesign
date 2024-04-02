class UpdateRecordAuditS2D:
    def __init__(self):

        self.updateKey = None

        self.recordId = None

        self.audit_R=None
        self.auditWhy_R=None
    def setUpdateRecordAudit(self,audit_R,auditWhy_R,updateKey):
        self.audit_R=audit_R
        self.auditWhy_R=auditWhy_R
        self.updateKey=updateKey
    def setRecordAuditBaseValues(self,recordId):

        self.recordId = recordId


    def getDaoDict(self):
        daoDict = {"recordId":self.recordId}
        if(self.updateKey == 1):
            daoDict["audit_R"] = 1
            daoDict["auditWhy_R"]=self.auditWhy_R
        elif(self.updateKey == 2):
            daoDict["audit_R"] = 2
            daoDict["auditWhy_R"]=self.auditWhy_R
        return daoDict

    def getSqlValues(self):
        if (self.updateKey == 1):
            return "audit_R=:audit_R,auditWhy_R=:auditWhy_R"
        elif (self.updateKey == 2):
            return "audit_R=:audit_R,auditWhy_R=:auditWhy_R"