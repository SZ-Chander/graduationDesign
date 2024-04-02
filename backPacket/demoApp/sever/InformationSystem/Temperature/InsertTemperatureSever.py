from backPacket.demoApp.dao.InformationSystem.Temperature import InsertTemperatureDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import InsertTemperatureS2D

"""
类名：insertTemperatureSever
描述：新增体温信息Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class InsertTemperatureSever:

    """
    功能阐述:新建体温信息功能Sever层主入口
    @:date 2023/4/19
    @:author 常舜志
    """
    def insertTemperatureSever(self,departTemperature):
        try:
            dateStringFormat = "%Y-%m-%d %H:%M:%S"
            dateStringFormat2="%Y%m%d%H%M%S"
            departId = departTemperature.getDepartId()
            staff = departTemperature.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departTemperature.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                # patientId,nursingDate,createDate,userId,
                # nursingWhat,inAndOut,selfCareAssess,nursingRounds

                temperature = departTemperature.getNursingList()
                createDate = usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat)
                audit=0
                TempId="t"+temperature.getpatientId()+usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat2)
                # 装载参数进入TO
                # patientId,createDate,userId,testDate,temperature,
                # pulse,breathe,shit,inWater,pee,weight,bloodPressure
                insertTemperatureS2D = InsertTemperatureS2D.InsertTemperatureS2D()
                insertTemperatureS2D.setInsertTemperatureBaseMess(
                    patientId=temperature.getpatientId(),createDate=createDate,userId=temperature.getuserId(),
                    testDate=temperature.gettestDate(),temperature=temperature.gettemperature(),pulse=temperature.getpulse(),
                    breathe=temperature.getbreathe(),shit=temperature.getshit(),inWater=temperature.getinWater(),
                    pee=temperature.getpee(),weight=temperature.getweight(),bloodPressure=temperature.getbloodPressure(),
                    audit=audit,TempId=TempId
                    )
                # 调用dao层
                insertTemperatureDao = InsertTemperatureDao.InsertTemperatureDao()
                rowCount = insertTemperatureDao.insertTemperatureDao(insertTemperatureS2D)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def setDepartName(self,depart):
        departMessList = depart.getStaff().getDepart()
        departId = depart.getDepartId()
        for departMess in departMessList:
            if(departId == departMess[0]):
                depart.setDepartName(departMess[1])
                break