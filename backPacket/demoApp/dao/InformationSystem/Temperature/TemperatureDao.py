from backPacket.demoApp.dto import Temperature
from flask import current_app
from sqlalchemy import text
"""
类名：Temperature
描述：体温单Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/2
备注：
"""
class TemperatureDao:
    def __init__(self):
        self.temperatureTable = "View_Temperature"
        self.TempTable="View_TempTable"
        self.db = current_app.config['db']

    """
    功能阐述:体温单Dao层主入口
    @:date 2023/4/2
    @:author 马梓洋
    """
    def temperatureDao(self,depart):
        key=depart.getselectKey()
        if(key==0):
            sqlStr = "select * from {} where departId=:departId and testDate BETWEEN :BeginDate AND :EndDate".format(self.temperatureTable)
            retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId(),BeginDate=depart.getBeginDate(),EndDate=depart.getEndDate())))
        elif(key==1):
            sqlStr = "select * from {} where departId=:departId and TempTableId=:TempTableId".format(self.temperatureTable)
            retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId(),TempTableId=depart.getTempTableId())))
        recordList = []
        for temperature in retData:
            record = Temperature.Temperature()
            record.setTemperature1(
                patientId=temperature[0],patientName=temperature[1],patientAge=temperature[2],departId=temperature[3],
                departName=temperature[4],testDate=temperature[5],temperature=temperature[6],pulse=temperature[7],
                breathe=temperature[8],shit=temperature[9],inWater=temperature[10],pee=temperature[11],
                weight=temperature[12],bloodPressure=temperature[13],createDate=temperature[14],userName=temperature[15],
                audit=temperature[16],auditWhy=temperature[17],TempId=temperature[18],TempTableId=temperature[19]
            )
            recordList.append(record)
        depart.setTemperatureList(recordList)
        return depart