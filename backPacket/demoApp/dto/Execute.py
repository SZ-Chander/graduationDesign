import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：Execute
描述：执行单信息实体dto（对应数据库View_Execute视图）
入参：无初始化入参，通过Set方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/3/31
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class Execute:
    def __init__(self):
        self.patientId = None
        self.patientName = None
        self.visitId = None
        self.departId = None
        self.departName = None
        self.executeId = None
        self.executeSubId = None
        self.executeItem = None
        self.executeSubItem = None
        self.staffId = None
        self.staffName = None
        self.executeLabel = None
        self.creatTime = None
        self.executeTime = None
        self.executeKey = None
        self.typeCode = None
        self.typeName = None
        self.typeLabel = None
        self.completeKey = None
        self.completeDate = None
        self.bedNo = None
        self.creatStaff = None

    def setExecute(self,patientId,patientName,visitId,departId,departName,executeId,executeSubId,executeItem,executeSubItem,
                   staffId,staffName,executeLabel,creatTime,executeTime,executeKey,typeCode,typeName,typeLabel,
                   completeKey,completeDate,bedNo,creatStaff):
        self.patientId = str(patientId)
        self.patientName = str(patientName)
        self.visitId = int(visitId)
        self.departId = str(departId)
        self.departName = str(departName)
        self.executeId = str(executeId)
        self.executeSubId = str(executeSubId)
        self.executeItem = str(executeItem)
        self.executeSubItem = str(executeSubItem)
        self.staffId = str(staffId)
        self.staffName = str(staffName)
        self.executeLabel = str(executeLabel)
        self.creatTime = usefulTools.UsefulTools().dateTime2String(creatTime,dateStringFormat)
        self.executeTime = usefulTools.UsefulTools().dateTime2String(executeTime,dateStringFormat)
        self.executeKey = int(executeKey)
        self.typeCode = str(typeCode)
        self.typeName = str(typeName)
        self.typeLabel = str(typeLabel)
        self.completeKey = int(completeKey)
        self.completeDate = usefulTools.UsefulTools().dateTime2String(completeDate,dateStringFormat)
        self.bedNo = str(bedNo)
        self.creatStaff = str(creatStaff)
    def setCreatStaff(self,createStaff):
        self.creatStaff = createStaff
    def setTypeLabel(self,typeLabel):
        self.typeLabel = typeLabel
    def setTypeCode(self,typeCode):
        self.typeCode = typeCode
    def setExecuteItem(self,executeItem):
        self.executeItem = executeItem
    def setExecuteSubItem(self,executeSubItem):
        self.executeSubItem = executeSubItem
    def setDepartId(self,departId):
        self.departId = departId
    def getDepartId(self):
        return self.departId
    def setExecuteTime(self,executeTime):
        self.executeTime = executeTime
    def setExecuteKey(self,executeKey):
        self.executeKey = executeKey
    def setCompleteDate(self,completeDate):
        self.completeDate = completeDate
    def setCompleteKey(self,completeKey):
        self.completeKey = completeKey
    def setExecuteLabel(self,executeLabel):
        self.executeLabel = executeLabel
    def setStaffId(self,staffId):
        self.staffId = staffId
    def getCompleteKey(self):
        return self.completeKey
    def getCompleteDate(self):
        return self.completeDate
    def getExecuteTime(self):
        return self.executeTime
    def getExecuteKey(self):
        return self.executeKey
    def setPatientId(self,patientId):
        self.patientId = patientId
    def setVisitId(self,visitId):
        self.visitId = int(visitId)
    def setExecuteId(self,executeId):
        self.executeId = executeId
    def setExecuteSubId(self,executeSubId):
        self.executeSubId = int(executeSubId)
    def getPatientId(self):
        return self.patientId
    def getvisitId(self):
        return self.visitId
    def getExecuteId(self):
        return self.executeId
    def getExecuteSubId(self):
        return self.executeSubId
    def getExecuteLabel(self):
        return self.executeLabel
    def getExecuteItem(self):
        return self.executeItem
    def getExecuteSubItem(self):
        return self.executeSubItem
    def getTypeCode(self):
        return self.typeCode
    def getCreatStaff(self):
        return self.creatStaff
    def getStaffId(self):
        return self.staffId