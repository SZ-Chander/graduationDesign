
class DepartStaff:
    def __init__(self):
        self.staffList = None
        self.staff = None
        self.departId = None
        self.departName = None
        self.selectKey=None
        self.userId=None
        self.name=None
    def setDepart(self,departstaffList,staff):
        self.departstaffList = departstaffList
        self.staff = staff
    def setStaff(self,staff):
        self.staff = staff
    def setStaffList(self,staffList):
        self.staffList = staffList
    def getstaffList(self):
        return self.staffList
    def getDepartId(self):
        return self.departId
    def setDepartName(self,departName):
        self.departName = departName
    def setDepartId(self,departId):
        self.departId = departId
    def getStaff(self):
        return self.staff
    def getname(self):
        return self.name
    def getselectKey(self):
        return self.selectKey

    def getuserId(self):
        return self.userId
    def setSelectKey(self,selectKey):
        self.selectKey=selectKey
    def setUserId(self,userId):
        self.userId=userId
    def setName(self,name):
        self.name=name
    """
    功能阐述:快速将全dto完全字典化的快速方法
    @:date 2023/4/1
    @:author 马梓洋
    """
    def obj2Dict(self):
        self.staff = self.staff.__dict__
        staffMess = []
        for nursing in self.staffList:
            staffMess.append(nursing.__dict__)
        self.staffList = staffMess