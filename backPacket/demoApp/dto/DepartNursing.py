
class DepartNursing:
    def __init__(self):
        self.nursingList = None
        self.staff = None
        self.departId = None
        self.departName = None
        self.selectKey=None
        self.patientId=None
        self.recordId=None
        self.planId=None
        self.BeginDate=None
        self.EndDate=None
    def setDepart(self,departNursingList,staff):
        self.departNursingList = departNursingList
        self.staff = staff
    def setStaff(self,staff):
        self.staff = staff
    def setNursingList(self,nursingList):
        self.nursingList = nursingList
    def getNursingList(self):
        return self.nursingList
    def getDepartId(self):
        return self.departId
    def setDepartName(self,departName):
        self.departName = departName
    def setDepartId(self,departId):
        self.departId = departId
    def getStaff(self):
        return self.staff

    def getselectKey(self):
        return self.selectKey
    def getrecordId(self):
        return self.recordId
    def getpatientId(self):
        return self.patientId
    def getplanId(self):
        return self.planId
    def getBeginDate(self):
        return self.BeginDate
    def getEndDate(self):
        return self.EndDate

    def setSelectKey(self,selectKey):
        self.selectKey=selectKey
    def setPatientId(self,patientId):
        self.patientId=patientId
    def setRecordId(self,recordId):
        self.recordId=recordId
    def setPlanId(self,planId):
        self.planId=planId
    def setBeginDate(self,BeginDate):
        self.BeginDate=BeginDate
    def setEndDate(self,EndDate):
        self.EndDate=EndDate


    """
    功能阐述:快速将全dto完全字典化的快速方法
    @:date 2023/4/1
    @:author 马梓洋
    """
    def obj2Dict(self):
        self.staff = self.staff.__dict__
        nursingMess = []
        for nursing in self.nursingList:
            nursingMess.append(nursing.__dict__)
        self.nursingList = nursingMess