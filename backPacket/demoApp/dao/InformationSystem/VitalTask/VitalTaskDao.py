from backPacket.demoApp.dto.InformationSystem import Bed, Patient
from flask import current_app
from sqlalchemy import text
"""
类名：vitalTaskDao
描述：床位一览卡Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
备注：
"""
class VitalTaskDao:
    def __init__(self):
        self.staffMessTable = "View_Staff_DepartMess"
        self.departMessTable = "View_inPatient_Mess"
        self.bedMessTable = "Table_depart_Bed_Mess"
        self.db = current_app.config['db']

    """
    功能阐述: 床位一览卡功能Dao层主入口
    @:date 2023/3/28
    @:author 常舜志
    """
    def vitalTaskDao(self,depart):
        # 读取科室病人列表
        sqlStr = "select * from {} where departId=:departId".format(self.departMessTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId())))
        patientList = []
        for patientMess in retData:
            patient = Patient.Patient()
            patient.setPatient(patientMess[0],patientMess[1],patientMess[2],patientMess[3],
                               patientMess[4],patientMess[5],patientMess[6],patientMess[7],
                               patientMess[8],patientMess[9],patientMess[10])
            patientList.append(patient)
        # 读取科室床位列表
        sqlStr = "select * from {} where departId=:departId".format(self.bedMessTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId())))
        bedDictMess = self.analysBedMess(retData)
        # 按照病人bedNo装入床位列表
        bedList = []
        for checkPatient in patientList:
            patientBedNo = checkPatient.getBedNo()
            if(patientBedNo in bedDictMess):
                bedDictMess[patientBedNo].setPatient(checkPatient)
        for bedKey in bedDictMess:
            bedMess = bedDictMess[bedKey]
            bedStr = "{}床".format(bedMess.getBedNo())
            bedMess.setBedNo(bedStr)
            bedList.append(bedDictMess[bedKey])
        # 完成装配，变为bed列表
        depart.setDepartBed(bedList)
        return depart

    def analysBedMess(self,inputMess):
        usefulMess = inputMess[0]
        departId = usefulMess[0]
        bedRangeStr = usefulMess[1]
        rangeMess = bedRangeStr.split("$")
        messList = []
        bedDict = {}
        for messNo in range(len(rangeMess)):
            if(messNo == 0):
                mess = int(rangeMess[messNo])
                for bedNo in range(1,mess+1):
                    messList.append(str(bedNo))
            else:
                messList.append(rangeMess[messNo])
        for bedMess in messList:
            bed = Bed.Bed()
            bed.setBedNo(bedMess)
            bed.setDepartId(departId)
            bedDict[bedMess] = bed
        return bedDict