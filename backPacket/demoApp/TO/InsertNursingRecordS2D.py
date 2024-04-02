class InsertNursingRecordS2D:
    def __init__(self):
        self.patientId = None
        self.nursingDate = None
        self.createDate = None
        self.userId = None
        self.nursingWhat = None
        self.Inwater = None
        self.selfCareAssess = None
        self.nursingRounds = None
        self.recordId=None
        self.audit_R=None
        self.audit_A=None
        self.Outwater=None
    def setInsertNursingRecordBaseMess(self,patientId,nursingDate,createDate,userId,Outwater,
                                     nursingWhat,Inwater,selfCareAssess,nursingRounds,recordId,audit_R,audit_A):
        self.patientId = str(patientId)
        self.nursingDate = nursingDate
        self.createDate = createDate
        self.userId = str(userId)
        self.nursingWhat = str(nursingWhat)
        self.Inwater = str(Inwater)
        self.selfCareAssess = str(selfCareAssess)
        self.nursingRounds = nursingRounds
        self.recordId=recordId
        self.audit_R=audit_R
        self.audit_A=audit_A
        self.Outwater=Outwater
    def getSqlValuesStr(self):
        return ":patientId,:nursingDate,:createDate,:userId,:nursingWhat,:Inwater,:selfCareAssess,:nursingRounds,:recordId,:audit_R,:audit_A,:Outwater"
    def getSqlFormatStr(self):
        return "patientId,nursingDate,createDate,userId,nursingWhat,Inwater,selfCareAssess,nursingRounds,recordId,audit_R,audit_A,Outwater"