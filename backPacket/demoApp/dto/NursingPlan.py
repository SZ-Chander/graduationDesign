import datetime

import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：NursingPlan
描述：护理计划实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/3/30
备注：实体类修改后务必进行全流程调试！
"""

dateStringFormat = "%Y-%m-%d %H:%M:%S"

class NursingPlan:
    def __init__(self):
        self.planId = None
        self.visitId = None
        self.planStatus = None
        self.patientDepartId = None
        self.departName = None
        self.patientName = None
        self.patientId = None
        self.nursingPlan = None
        self.planEmergency = None
        self.patientStatus = None
        self.lastUpdateDate = None
        self.createDate = None
        self.planUserId=None
        self.planUser = None
        self.stopDate = None
        self.stopWhy = None
        self.stopUser = None
        self.audit =None
        self.auditWhy=None
    def setNursingPlan1(self,planId,visitId,planStatus,patientDepartId,departName,patientName,patientId,nursingPlan,planEmergency,
                        patientStatus,lastUpdateDate,createDate,planUser,stopDate,stopWhy,stopUser,audit,auditWhy):
        self.planId = str(planId)
        self.visitId = int(visitId)
        self.planStatus = int(planStatus)
        self.patientDepartId = str(patientDepartId)
        self.departName = str(departName)
        self.patientName = str(patientName)
        self.patientId = str(patientId)
        self.nursingPlan = str(nursingPlan)
        self.planEmergency = str(planEmergency)
        self.patientStatus = str(patientStatus)
        self.lastUpdateDate = usefulTools.UsefulTools().dateTime2String(lastUpdateDate,dateStringFormat)
        self.createDate = usefulTools.UsefulTools().dateTime2String(createDate,dateStringFormat)
        self.planUser = str(planUser)
        self.stopDate = usefulTools.UsefulTools().dateTime2String(stopDate,dateStringFormat)
        self.stopWhy = str(stopWhy)
        self.stopUser = str(stopUser)
        self.audit= audit
        self.auditWhy=auditWhy
    def setLastUpdateDate(self):
        self.lastUpdateDate = datetime.datetime.now()

    def setStopDate(self):
        self.stopDate = datetime.datetime.now()

    def setPlanStatus(self,planStatus):
        self.planStatus = planStatus

    def setNursingPlan2(self,nursingPlan):
        self.nursingPlan=nursingPlan

    def setPlanEmergency(self,planEmergency):
        self.planEmergency=planEmergency

    def setPatientStatus(self,patientStatus):
        self.patientStatus=patientStatus

    def setPlanUserId(self,planUserId):
        self.planUserId=planUserId

    def setPatientId(self,patientId):
        self.patientId = patientId

    def setVisitId(self,visitId):
        self.visitId = visitId

    def setPlanId(self,planId):
        self.planId = planId

    def setStopUser(self,stopUser):
        self.stopUser = stopUser

    def setStopWhy(self,stopWhy):
        self.stopWhy = stopWhy

    def setAudit(self,audit):
        self.audit=audit
    def setAuditWhy(self,auditWhy):
        self.auditWhy=auditWhy

    def getlastUpdateDate(self):
        return self.lastUpdateDate

    def getstopDate(self):
        return self.stopDate

    def getplanStatus(self):
        return self.planStatus

    def getpatientId(self):
        return self.patientId

    def getvisitId(self):
        return self.visitId

    def getplanId(self):
        return self.planId

    def getnursingPlan(self):
        return self.nursingPlan
    def getplanEmergency(self):
        return self.planEmergency
    def getpatientStatus(self):
        return self.patientStatus
    def getplanUserId(self):
        return self.planUserId
    def getstopUser(self):
        return self.stopUser

    def getstopWhy(self):
        return self.stopWhy

    def getaudit(self):
        return self.audit
    def getauditWhy(self):
        return self.auditWhy

    def setDepartId(self,patientDepartId):
        self.patientDepartId = patientDepartId

    def getDepartId(self):
        return self.patientDepartId
