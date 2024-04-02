class InsertNursingPlanS2D:
    def __init__(self):
        self.planId = None
        self.patientId = None
        self.visitId = None
        self.dischargeKey = None
        self.planStatus = None
        self.nursingPlan = None
        self.planEmergency = None
        self.patientStatus = None
        self.lastUpdateDate = None
        self.createDate = None
        self.planUserId = None
        self.stopDate = None
        self.stopWhy = None
        self.stopUserId = None
        self.audit=None
    def setInsertNursingPlanBaseMess(self,planId,patientId,visitId,dischargeKey,planStatus,
                                 nursingPlan,planEmergency,patientStatus,lastUpdateDate,createDate,
                                 planUserId,audit):
        self.planId = str(planId)
        self.patientId = str(patientId)
        self.visitId = int(visitId)
        self.dischargeKey = int(dischargeKey)
        self.planStatus = int(planStatus)
        self.nursingPlan = str(nursingPlan)
        self.planEmergency = str(planEmergency)
        self.patientStatus = str(patientStatus)
        self.lastUpdateDate = lastUpdateDate
        self.createDate = createDate
        self.planUserId = str(planUserId)
        self.audit=int(audit)

    def getSqlValuesStr(self):
        return ":planId,:patientId,:visitId,:dischargeKey,:planStatus,:nursingPlan,:planEmergency,:patientStatus,:lastUpdateDate,:createDate,:planUserId,:audit"
    def getSqlFormatStr(self):
        return "planId,patientId,visitId,dischargeKey,planStatus,nursingPlan,planEmergency,patientStatus,lastUpdateDate,createDate,planUserId,audit"