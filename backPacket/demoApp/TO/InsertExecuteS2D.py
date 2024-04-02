class InsertExecuteS2D:
    def __init__(self):
        self.patientId = None
        self.visitId = None
        self.executeId = None
        self.executeSubId = None
        self.executeItem = None
        self.executeSubItem = None
        self.staffId = None
        self.executeLabel = None
        self.creatTime = None
        self.executeTime = None
        self.executeKey = None
        self.typeCode = None
        self.completeKey = None
        self.completeDate = None
        self.creatStaff = None
    def setInsertExecuteBaseMess(self,patientId,visitId,executeId,executeSubId,executeItem,
                                 executeSubItem,staffId,executeLabel,creatTime,executeKey,
                                 completeKey,typeCode,creatStaff):
        self.patientId = str(patientId)
        self.visitId = int(visitId)
        self.executeId = str(executeId)
        self.executeSubId = int(executeSubId)
        self.executeItem = str(executeItem)
        self.executeSubItem = str(executeSubItem)
        self.staffId = str(staffId)
        self.executeLabel = str(executeLabel)
        self.creatTime = creatTime
        self.typeCode = str(typeCode)
        self.creatStaff = str(creatStaff)
        self.completeKey = completeKey
        self.executeKey = executeKey
    def getSqlValuesStr(self):
        return ":patientId,:visitId,:executeId,:executeSubId,:executeItem,:executeSubItem,:staffId,:executeLabel,:creatTime,:executeTime,:executeKey,:typeCode,:completeKey,:completeDate,:creatStaff"
    def getSqlFormatStr(self):
        return "patientId,visitId,executeId,executeSubId,executeItem,executeSubItem,staffId,executeLabel,creatTime,executeTime,executeKey,typeCode,completeKey,completeDate,creatStaff"