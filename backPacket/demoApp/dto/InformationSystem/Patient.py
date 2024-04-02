"""
类名：Patient
描述：工作人员实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/3/24
备注：实体类修改后务必进行全流程调试！
"""
class Patient:
    def __init__(self):
        self.patientId = None
        self.patientName = None
        self.adminsionDate = None
        self.visitId = None
        self.patientDepartId = None
        self.adminsionSubDate = None
        self.dischargeDate = None
        self.dischargeKey = None
        self.patientAge = None
        self.nursingGrade = None
        self.bedNo = None
    """
    功能阐述:病人信息dto的set方法
    @:date 2023/03/29
    @:author 常舜志
    """
    def setPatient(self,patientId,patientName,adminsionDate,visitId,patientDepartId,adminsionSubDate,dischargeDate,dischargeKey,patientAge,nursingGrade,bedNo):
        self.patientId = patientId
        self.patientName = patientName
        self.adminsionDate = adminsionDate
        self.visitId = int(visitId)
        self.patientDepartId = patientDepartId
        self.adminsionSubDate = adminsionSubDate
        self.dischargeDate = dischargeDate
        self.dischargeKey = int(dischargeKey)
        self.patientAge = patientAge
        self.nursingGrade = int(nursingGrade)
        self.bedNo = bedNo
    """
    功能阐述: 床号的get方法
    @:date 2023/03/28
    @:author 常舜志
    """
    def getBedNo(self):
        return self.bedNo