import datetime

import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：NursingRecord
描述：护理记录实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/4/1
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class NursingRecord:
    def __init__(self):
        self.recordId = None
        self.patientId = None
        self.patientName = None
        self.patientAge = None
        self.departId = None
        self.departName = None
        self.nursingDate = None
        self.nursingWhat = None
        self.Inwater = None
        self.selfCareAssess = None
        self.nursingRounds= None
        self.Outwater = None
        self.userId=None
        self.createDate=None
        self.userName=None
        self.audit_R=None
        self.auditWhy_R=None
        self.audit_A=None
        self.auditWhy_A=None
    def setNursingRecord(self,recordId,patientName,patientAge,departId,departName,nursingDate,nursingWhat,Inwater,
                       selfCareAssess,nursingRounds,Outwater,userName,createDate,audit_R,auditWhy_R,
                         patientId):
        self.recordId=recordId
        self.patientName = patientName
        self.patientAge = patientAge
        self.departId = departId
        self.departName = departName
        self.nursingDate = usefulTools.UsefulTools().dateTime2String(nursingDate,dateStringFormat)
        self.nursingWhat = nursingWhat
        self.Inwater = Inwater
        self.selfCareAssess = selfCareAssess
        self.nursingRounds = nursingRounds
        self.Outwater = Outwater
        self.userName= userName
        self.createDate=usefulTools.UsefulTools().dateTime2String(createDate,dateStringFormat)
        self.audit_R=audit_R
        self.auditWhy_R=auditWhy_R
        self.patientId=patientId
    def getrecordId(self):
        return self.recordId

    def getnursingDate(self):
        return self.nursingDate
    def getnursingWhat(self):
        return self.nursingWhat
    def getinwater(self):
        return self.Inwater
    def getselfCareAssess(self):
        return self.selfCareAssess
    def getnursingRounds(self):
        return self.nursingRounds
    def getuserId(self):
        return self.userId
    def getpatientId(self):
        return self.patientId
    def getcreateDate(self):
        return self.createDate
    def getoutwater(self):
        return self.Outwater
    def getDepartId(self):
        return self.patientDepartId
    def getaudit_R(self):
        return self.audit_R
    def getaudit_A(self):
        return self.audit_A
    def getauditWhy_R(self):
        return self.auditWhy_R
    def getauditWhy_A(self):
        return self.auditWhy_A

    def setRecordId(self,recordId):
        self.recordId=recordId
    def setNursingDate(self,nursingDate):
        self.nursingDate=nursingDate
    def setNursingWhat(self,nursingWhat):
        self.nursingWhat=nursingWhat
    def setInwater(self,Inwater):
        self.Inwater=Inwater
    def setSelfCareAssess(self,selfCareAssess):
        self.selfCareAssess=selfCareAssess
    def setNursingRounds(self,nursingRounds):
        self.nursingRounds=nursingRounds
    def setUserId(self,userId):
        self.userId=userId
    def setPatientId(self,patientId):
        self.patientId=patientId
    def setCreateDate(self,createDate):
        self.createDate=createDate
    def setOutwater(self,Outwater):
        self.Outwater=Outwater
    def setDepartId(self,patientDepartId):
        self.patientDepartId = patientDepartId
    def setAudit_R(self,audit_R):
        self.audit_R=audit_R
    def setAudit_A(self,audit_A):
        self.audit_A=audit_A
    def setAuditWhy_R(self,auditWhy_R):
        self.auditWhy_R=auditWhy_R
    def setAuditWhy_A(self,auditWhy_A):
        self.auditWhy_A=auditWhy_A
