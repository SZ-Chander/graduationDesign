import datetime

import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：Temperature
描述：体温单实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/4/2
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class Temperature:
    def __init__(self):
        self.patientId = None
        self.patientName = None
        self.patientAge = None
        self.departId = None
        self.departName = None
        self.createDate = None
        self.testDate = None
        self.temperature = None
        self.pulse = None
        self.breathe = None
        self.shit = None
        self.inWater = None
        self.pee = None
        self.weight = None
        self.bloodPressure = None
        self.userName=None
        self.userId=None
        self.audit=None
        self.TempId=None
        self.auditWhy=None
        self.TempTableId=None
    def setTemperature1(self,patientId,patientName,patientAge,departId,departName,createDate,testDate,temperature,pulse,
                         breathe,shit,inWater,pee,weight,bloodPressure,userName,audit,auditWhy,TempId,TempTableId):

        self.patientId = patientId
        self.patientName = patientName
        self.patientAge = patientAge
        self.departId = departId
        self.departName = departName
        self.createDate=usefulTools.UsefulTools().dateTime2String(createDate,dateStringFormat)
        self.testDate = usefulTools.UsefulTools().dateTime2String(testDate,dateStringFormat)
        self.temperature = temperature
        self.pulse = pulse
        self.breathe = breathe
        self.shit = shit
        self.inWater = inWater
        self.pee = pee
        self.weight = weight
        self.bloodPressure = bloodPressure
        self.userName =userName
        self.audit=audit
        self.TempId=TempId
        self.auditWhy=auditWhy
        self.TempTableId=TempTableId
    def getDepartId(self):
        return self.patientDepartId

    def setDepartId(self,patientDepartId):
        self.patientDepartId = patientDepartId
    #testDate,temperature,pulse,breathe,shit,inWater,pee,weight,bloodPressure
    def gettestDate(self):
        return self.testDate
    def gettemperature(self):
        return self.temperature
    def getpulse(self):
        return self.pulse
    def getbreathe(self):
        return self.breathe
    def getshit(self):
        return self.shit
    def getinWater(self):
        return self.inWater
    def getpee(self):
        return self.pee
    def getweight(self):
        return self.weight
    def getbloodPressure(self):
        return self.bloodPressure
    def getuserId(self):
        return self.userId
    def getpatientId(self):
        return self.patientId
    def getcreateDate(self):
        return self.createDate
    def getaudit(self):
        return self.audit
    def getTempId(self):
        return self.TempId
    def getTempTableId(self):
        return self.TempTableId
    def getauditWhy(self):
        return self.auditWhy

    def setTestDate(self,testDate):
        self.testDate=testDate
    def setTemperature2(self,temperature):
        self.temperature=temperature
    def setPulse(self,pulse):
        self.pulse=pulse
    def setBreathe(self,breathe):
        self.breathe=breathe
    def setShit(self,shit):
        self.shit=shit
    def setInWater(self,inWater):
        self.inWater=inWater
    def setPee(self,pee):
        self.pee=pee
    def setWeight(self,weight):
        self.weight=weight
    def setBloodPressure(self,bloodPressure):
        self.bloodPressure=bloodPressure
    def setUserId(self,userId):
        self.userId=userId

    def setPatientId(self,patientId):
        self.patientId=patientId
    def setCreateDate(self,createDate):
        self.createDate=createDate
    def setAudit(self,audit):
        self.audit=audit
    def setTempId(self,TempId):
        self.TempId=TempId
    def setTempTableId(self,TempTableId):
        self.TempTableId=TempTableId
    def setAuditWhy(self,auditWhy):
        self.auditWhy=auditWhy