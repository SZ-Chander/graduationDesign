"""
类名：DepartVitalTask
描述：科室床位一览卡
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/3/28
备注：实体类修改后务必进行全流程调试！
"""
class DepartVitalTask:
    def __init__(self):
        self.departId = None
        self.departName = None
        self.departBed = None
        self.staff = None
    def setDepart(self,departId,departName,departBed,staff):
        self.departId = departId
        self.departName = departName
        self.departBed = departBed
        self.staff = staff

    def getDepartId(self):
        return self.departId
    def getStaff(self):
        return self.staff
    def setDepartId(self,departId):
        self.departId = departId
    def setDepartName(self,departName):
        self.departName = departName
    def setStaff(self,staff):
        self.staff = staff
    def setDepartBed(self,departBed):
        self.departBed = departBed
    """
    功能阐述:快速将全dto完全字典化的快速方法
    @:date 2023/03/28
    @:author 常舜志
    """
    def obj2Dict(self):
        self.staff = self.staff.__dict__
        bedMess = []
        for bed in self.departBed:
            bed.bedRe_Obj2Dict()
            bedMess.append(bed.__dict__)
        self.departBed = bedMess