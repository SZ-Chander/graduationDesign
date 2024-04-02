class InsertNursingAssessS2D:
    def __init__(self):
        self.patientId = None

        self.createDate = None
        self.lastUpDate=None
        self.userId = None
        self.recordId=None
        self.audit=None
    def setInsertNursingAssessBaseMess(self,patientId,lastUpDate,createDate,userId,
                                       recordId,audit):
        self.patientId = str(patientId)
        self.lastUpDate = lastUpDate
        self.createDate = createDate
        self.userId = str(userId)
        self.recordId=recordId
        self.audit=audit

    def getSqlValuesStr(self):
        return ":patientId,:lastUpDate,:createDate,:userId,:recordId,:audit"
    def getSqlFormatStr(self):
        return "patientId,lastUpDate,createDate,userId,recordId,audit"