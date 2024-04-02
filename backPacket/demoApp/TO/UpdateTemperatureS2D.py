class UpdateTemperatureS2D:
    def __init__(self):
        self.patientId = None
        self.createDate = None
        self.TempId=None
        self.testDate = None
        self.temperature = None
        self.pulse = None
        self.breathe = None
        self.shit = None
        self.inWater = None
        self.pee = None
        self.weight = None
        self.bloodPressure= None

    def setUpdateTemperature(self,testDate,temperature,pulse,breathe,shit,inWater,pee,weight,bloodPressure):#设置需要更新的字段

        self.testDate = testDate
        self.temperature = temperature
        self.pulse = pulse
        self.breathe = breathe
        self.shit = shit
        self.inWater = inWater
        self.pee = pee
        self.weight = weight
        self.bloodPressure = bloodPressure

    def setTemperatureBaseValues(self,patientId,TempId):#主键字段
        self.patientId = patientId
        self.TempId = TempId

    def getDaoDict(self):
        daoDict = {"patientId":self.patientId,"TempId":self.TempId}
        daoDict["testDate"] = self.testDate
        daoDict["temperature"] = self.temperature
        daoDict["pulse"] = self.pulse
        daoDict["breathe"] = self.breathe
        daoDict["shit"] = self.shit
        daoDict["inWater"] = self.inWater
        daoDict["pee"] = self.pee
        daoDict["weight"] = self.weight
        daoDict["bloodPressure"] = self.bloodPressure
        return daoDict


    def getSqlValues(self):
        return "testDate=:testDate,temperature=:temperature,pulse=:pulse,breathe=:breathe,shit=:shit,inWater=:inWater,pee=:pee,weight=:weight,bloodPressure=:bloodPressure"
