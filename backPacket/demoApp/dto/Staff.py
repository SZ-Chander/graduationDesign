"""
类名：Staff
描述：工作人员实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/3/24
备注：实体类修改后务必进行全流程调试！
"""
class Staff:
    def __init__(self):
        self.staffId = None
        self.staffName = None
        self.departCode = None
        self.departName = None
        self.staffAutority = None
        self.departIndex = None
    """
    功能阐述: 工作人员信息的set方法
    @:date 2023/03/28
    @:author 常舜志
    """
    def setStaff(self,staffId,staffName,departCode,departName,staffAutority):
        self.staffId = staffId
        self.staffName = staffName
        self.departCode = departCode
        self.departName = departName
        self.staffAutority = staffAutority
    def getStaff(self):
        return Staff.__dict__
    def setStaffId(self,staffId):
        self.staffId = staffId
    def getStaffName(self):
        return self.staffName
    def getStaffId(self):
        return self.staffId
    """
    功能阐述:检查该dto所承载之信息是否为管理员信息
    @:date 2023/03/27
    @:author 常舜志
    """
    def checkAdmin(self):
        ramList = []
        for code in self.departCode:
            if(code != "000"):
                ramList.append(code)
        self.departCode = ramList
        ramList = []
        for name in self.departName:
            if(name != "管理员"):
                ramList.append(name)
        self.departName = ramList
    """
    功能阐述:将科室departCode和departName信息打包返回的get方法
    @:date 2023/03/27
    @:author 常舜志
    """
    def getDepart(self):
        departList = []
        self.departIndex = {}
        try:
            assert len(self.departName) == len(self.departCode)
            for num in range(len(self.departCode)):
                self.departIndex[self.departCode[num]] = self.departName[num]
                departTuple = (self.departCode[num],self.departName[num])
                departList.append(departTuple)
        except:
            pass
        finally:
            return departList
    def getDepartCode(self):
        return self.departCode
    def getStaffAutority(self):
        return self.staffAutority
    def setStaffName(self,staffName):
        self.staffName = staffName
    def setDepartCode(self,departCode):
        self.departCode = departCode
    def setStaffAutority(self,staffAutority):
        self.staffAutority = staffAutority
