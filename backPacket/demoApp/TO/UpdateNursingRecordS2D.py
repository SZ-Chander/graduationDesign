class UpdateNursingRecordS2D:
    def __init__(self):
        self.nursingDate = None
        self.nursingWhat = None
        self.Inwater=None
        self.selfCareAssess=None
        self.nursingRounds=None
        self.recordId=None
        self.patientId = None
        self.userId = None
        self.sqlValues = None
        self.Outwater=None
    def setUpdateNursingRecord(self,nursingDate,nursingWhat,Inwater,selfCareAssess,nursingRounds,Outwater):#设置需要更新的字段

        self.nursingDate = nursingDate
        self.nursingWhat = nursingWhat
        self.Inwater = Inwater
        self.selfCareAssess = selfCareAssess
        self.nursingRounds = nursingRounds
        self.Outwater = Outwater
    def setNursingRecordBaseValues(self,recordId):#主键字段
        self.recordId = recordId
    def getDaoDict(self):
        daoDict = {"recordId":self.recordId}
        daoDict["nursingDate"] = self.nursingDate
        daoDict["nursingWhat"] = self.nursingWhat
        daoDict["Inwater"] = self.Inwater
        daoDict["selfCareAssess"] = self.selfCareAssess
        daoDict["nursingRounds"] = self.nursingRounds
        daoDict["Outwater"]=self.Outwater
        return daoDict


    def getSqlValues(self):
        return "nursingDate=:nursingDate,nursingWhat=:nursingWhat,Inwater=:Inwater,selfCareAssess=:selfCareAssess,nursingRounds=:nursingRounds,Outwater=:Outwater"
