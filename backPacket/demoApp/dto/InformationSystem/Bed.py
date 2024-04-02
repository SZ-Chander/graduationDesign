"""
类名：Bed
描述：床位实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/3/29
备注：实体类修改后务必进行全流程调试！
"""
class Bed:
    def __init__(self):
        self.departId = None
        self.bedNo = None
        self.patient = None
    def setBed(self,departId,bedNo,patient):
        self.bedNo = bedNo
        self.patient = patient
        self.departId = departId
    def setBedNo(self,bedNo):
        self.bedNo = bedNo
    def setDepartId(self,departId):
        self.departId = departId
    def setPatient(self,patient):
        self.patient = patient
    def getBedNo(self):
        return self.bedNo
    """
    功能阐述:将床位dto快速字典化的方法
    @:date 2023/03/29
    @:author 常舜志
    """
    def bedRe_Obj2Dict(self):
        if(self.patient != None):
            self.patient = self.patient.__dict__