from backPacket.demoApp.dao.InformationSystem.Temperature import CreateTempTableDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import CreateTempTableS2D

"""
类名：CreateTempTableSever
描述：创建体温单功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/18
"""
class CreateTempTableSever:

    """
    功能阐述:创建体温单功能Sever层主入口
    @:date 2023/4/18
    @:author 马梓洋
    """
    def createTempTableSever(self,departTemperature):
        try:

            departId = departTemperature.getDepartId()
            staff = departTemperature.getStaff()
            key = self.checkKey(departTemperature)

            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departTemperature.getDepartId() in staff.getDepartCode()):
                createTempTableDao = CreateTempTableDao.CreateTempTableDao()
                rowCount = createTempTableDao.createTempTableDao(key)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departTemperature):
        dateStringFormat2="%Y%m%d%H%M%S%f"#精确到毫秒
        createTempTableS2D = CreateTempTableS2D.CreateTempTableS2D()
        temperature = departTemperature.gettemperatureList()
        TempTableId="T"+usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat2)

        #testDate,temperature,pulse,breathe,shit,inWater,pee,weight,bloodPressure
        createTempTableS2D.setTempTableId(TempTableId)
        departTemperature.setTempTableId(TempTableId)
        createTempTableS2D.setTempIdList(temperature.getTempIdList())

        return createTempTableS2D