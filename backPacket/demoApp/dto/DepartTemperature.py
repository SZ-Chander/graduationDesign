
class DepartTemperature:
    def __init__(self):
        self.temperatureList = None
        self.staff = None
        self.departId = None
        self.departName = None
        self.selectKey=None
        self.patientId=None
        self.BeginDate=None
        self.EndDate=None
        self.TempId=None
        self.TempIdList=None
        self.TempTableId=None
    def setDepart(self,departNursingList,staff):
        self.departNursingList = departNursingList
        self.staff = staff
    def setStaff(self,staff):
        self.staff = staff
    def setTemperatureList(self,temperatureList):
        self.temperatureList = temperatureList
    def gettemperatureList(self):
        return self.temperatureList
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
    def getBeginDate(self):
        return self.BeginDate
    def getEndDate(self):
        return self.EndDate
    def getpatientId(self):
        return self.patientId
    def getTempId(self):
        return self.TempId
    def getTempIdList(self):
        return self.TempIdList
    def getTempTableId(self):
        return self.TempTableId

    def setSelectKey(self,selectKey):
        self.selectKey=selectKey
    def setPatientId(self,patientId):
        self.patientId=patientId
    def setBeginDate(self,BeginDate):
        self.BeginDate=BeginDate
    def setEndDate(self,EndDate):
        self.EndDate=EndDate
    def setTempId(self,TempId):
        self.TempId=TempId
    def setTempIdList(self,TempIdList):
        self.TempIdList=TempIdList
    def setTempTableId(self,TempTableId):
        self.TempTableId=TempTableId
    """
    功能阐述:快速将全dto完全字典化的快速方法
    @:date 2023/4/1
    @:author 马梓洋
    """
    def obj2Dict(self):
        self.staff = self.staff.__dict__
        temperatureMess = []
        for nursing in self.temperatureList:
            temperatureMess.append(nursing.__dict__)
        self.temperatureList = temperatureMess