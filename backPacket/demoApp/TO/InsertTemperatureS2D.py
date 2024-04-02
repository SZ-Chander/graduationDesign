class InsertTemperatureS2D:
    def __init__(self):
        self.patientId = None
        self.createDate = None
        self.userId = None
        self.testDate = None
        self.temperature = None
        self.pulse = None
        self.breathe = None
        self.shit = None
        self.inWater=None
        self.pee=None
        self.weight=None
        self.bloodPressure=None
        self.audit=None
        self.TempId=None
    def setInsertTemperatureBaseMess(self,patientId,createDate,userId,testDate,temperature,
                                       pulse,breathe,shit,inWater,pee,weight,bloodPressure,audit,TempId):
        self.patientId = str(patientId)
        self.createDate = createDate
        self.userId = str(userId)
        self.testDate = testDate
        self.temperature = str(temperature)
        self.pulse = str(pulse)
        self.breathe = str(breathe)
        self.shit=str(shit)
        self.inWater=str(inWater)
        self.pee=str(pee)
        self.weight=str(weight)
        self.bloodPressure=str(bloodPressure)
        self.audit= int(audit)
        self.TempId=str(TempId)
    def getSqlValuesStr(self):
        return ":patientId,:createDate,:userId,:testDate,:temperature,:pulse,:breathe,:shit,:inWater,:pee,:weight,:bloodPressure,:audit,:TempId"
    def getSqlFormatStr(self):
        return "patientId,createDate,userId,testDate,temperature,pulse,breathe,shit,inWater,pee,weight,bloodPressure,audit,TempId"