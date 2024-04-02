class UpdateNursingAssessS2D:
    def __init__(self):
        self.nursingAssess=None
        self.recordId=None
        self.patientId = None
        self.userId = None
        self.sqlValues = None
        self.createDate = None
        self.lastUpDate = None
        self.nursingAssess = None
        self.allergy = None
        self.conscious = None
        self.position=None
        self.communication=None
        self.limb=None
        self.swallow=None
        self.eyes=None
        self.food=None
        self.shit=None
        self.pee=None
        self.chronic=None
        self.audit=None
        self.auditWhy=None
        self.selectKey=None
        self.userId=None
# lastUpDate,name,
# nursingAssess,allergy,conscious,position,communication,limb,swallow,eyes,food,shit,pee,chronic,
# audit,auditWhy,patientId
    def setUpdateNursingAssess(self,nursingAssess,lastUpDate,userId,allergy,conscious,position,communication,limb,
                               swallow,eyes,food,shit,pee,chronic
                               ):#设置需要更新的字段

        self.nursingAssess = nursingAssess
        self.lastUpDate=lastUpDate
        self.userId=userId
        self.allergy=allergy
        self.conscious=conscious
        self.position=position
        self.communication=communication
        self.limb=limb
        self.swallow=swallow
        self.eyes=eyes
        self.food=food
        self.shit=shit
        self.pee=pee
        self.chronic=chronic

    def setNursingAssessBaseValues(self,recordId):#主键字段
        self.recordId = recordId
    def getDaoDict(self):
        daoDict = {"recordId":self.recordId}
        daoDict["nursingAssess"] = self.nursingAssess
        daoDict["lastUpDate"]=self.lastUpDate
        daoDict["userId"]=self.userId
        daoDict["allergy"]=self.allergy
        daoDict["conscious"]=self.conscious
        daoDict["position"]=self.position
        daoDict["communication"]=self.communication
        daoDict["limb"]=self.limb
        daoDict["swallow"]=self.swallow
        daoDict["eyes"]=self.eyes
        daoDict["food"]= self.food
        daoDict["shit"]=self.shit
        daoDict["pee"]=self.pee
        daoDict["chronic"]=self.chronic
        return daoDict


    def getSqlValues(self):
        return "nursingAssess=:nursingAssess,lastUpDate=:lastUpDate,userId=:userId,allergy=:allergy,conscious=:conscious,position=:position,communication=:communication,limb=:limb,swallow=:swallow,eyes=:eyes,food=:food,shit=:shit,pee=:pee,chronic=:chronic"
