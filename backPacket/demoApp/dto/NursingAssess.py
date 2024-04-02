import backPacket.demoApp.tools.usefulTools as usefulTools
import datetime
"""
类名：NursingAssess
描述：护理记录实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/4/1
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class NursingAssess:
    def __init__(self):
        self.patientName = None
        self.patientAge = None
        self.recordId = None
        self.departId = None
        self.departName = None
        self.createDate = None
        self.lastUpDate = None
        self.name = None
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
    def setNursingAssess1(self,patientName1,patientAge,recordId,departId,departName,createDate,lastUpDate,name,
                         nursingAssess,allergy,conscious,position,communication,limb,swallow,eyes,food,shit,pee,chronic,
                         audit,auditWhy,patientId):
        self.patientName = patientName1
        self.patientAge = patientAge
        self.recordId = recordId
        self.departId = departId
        self.departName = departName
        self.createDate = usefulTools.UsefulTools().dateTime2String(createDate,dateStringFormat)
        self.lastUpDate = usefulTools.UsefulTools().dateTime2String(lastUpDate,dateStringFormat)
        self.name = name
        self.nursingAssess = nursingAssess
        self.allergy = allergy
        self.conscious = conscious
        self.position=position
        self.communication=communication
        self.limb=limb
        self.swallow=swallow
        self.eyes=eyes
        self.food=food
        self.shit=shit
        self.pee=pee
        self.chronic=chronic
        self.audit=audit
        self.auditWhy=auditWhy
        self.patientId=patientId
    def getselectKey(self):
        return self.selectKey

    def getpatientName(self):
        return self.patientName

    def getpatientAge(self):
        return self.patientAge
    def getrecordId(self):
        return self.recordId
    def getdepartId(self):
        return self.departId
    def getdepartName(self):
        return self.departName
    def getcreateDate(self):
        return self.createDate
    def getlastUpDate(self):
        return self.lastUpDate
    def getname(self):
        return self.name
    def getnursingAssess(self):
        return self.nursingAssess
    def getallergy(self):
        return self.allergy
    def getconscious(self):
        return self.conscious
    def getposition(self):
        return self.position
    def getcommunication(self):
        return self.communication
    def getlimb(self):
        return self.limb
    def getswallow(self):
        return self.swallow
    def geteyes(self):
        return self.eyes
    def getfood(self):
        return self.food
    def getshit(self):
        return self.shit
    def getpee(self):
        return self.pee
    def getchronic(self):
        return self.chronic
    def getaudit(self):
        return self.audit
    def getauditWhy(self):
        return self.auditWhy
    def getpatientId(self):
        return self.patientId
    def getuserId(self):
        return self.userId
# recordId,departId,createDate,lastUpDate,
# nursingAssess,allergy,conscious,position,communication,limb,swallow,eyes,food,shit,pee,chronic,
# audit,auditWhy
    def setSelectKey(self,selectKey):
        self.selectKey=selectKey
    def setPatientId(self,patientId):
        self.patientId=patientId
    def setRecordId(self,recordId):
        self.recordId=recordId


    def setLastUpDate(self,lastUpDate):
        self.lastUpDate=lastUpDate
    def setNursingAssess2(self,nursingAssess):
        self.nursingAssess=nursingAssess
    def setAllergy(self,allergy):
        self.allergy=allergy

    def setConscious(self,conscious):
        self.conscious=conscious
    def setPosition(self,position):
        self.position=position
    def setCommunication(self,communication):
        self.communication=communication
    def setUserId(self,userId):
        self.userId=userId

    def setCreateDate(self,createDate):
        self.createDate=createDate

    def setDepartId(self,patientDepartId):
        self.patientDepartId = patientDepartId
    def setLimb(self,limb):
        self.limb=limb
    def setSwallow(self,swallow):
        self.swallow=swallow
    def setEyes(self,eyes):
        self.eyes=eyes
    def setFood(self,food):
        self.food=food
    def setShit(self,shit):
        self.shit=shit
    def setPee(self,pee):
        self.pee=pee
    def setChronic(self,chronic):
        self.chronic=chronic
    def setAudit(self,audit):
        self.audit=audit
    def setAuditWhy(self,auditWhy):
        self.auditWhy=auditWhy
