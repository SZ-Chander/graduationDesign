from backPacket.demoApp.dao.InformationSystem.Temperature import UpdateTemperatureDao
from backPacket.demoApp.TO import UpdateTemperatureS2D

"""
类名：UpdateTemperatureSever
描述：更新体温信息功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/18
"""
class UpdateTemperatureSever:

    """
    功能阐述:更新体温信息功能Sever层主入口
    @:date 2023/4/18
    @:author 马梓洋
    """
    def updateTemperatureSever(self,departTemperature):
        try:
            departId = departTemperature.getDepartId()
            staff = departTemperature.getStaff()
            key = self.checkKey(departTemperature)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departTemperature.getDepartId() in staff.getDepartCode()):
                updateTemperatureDao = UpdateTemperatureDao.UpdateTemperatureDao()
                rowCount = updateTemperatureDao.updateTemperatureDao(key)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departTemperature):
        updateTemperatureS2D = UpdateTemperatureS2D.UpdateTemperatureS2D()
        temperature = departTemperature.gettemperatureList()
#testDate,temperature,pulse,breathe,shit,inWater,pee,weight,bloodPressure
        updateTemperatureS2D.setUpdateTemperature(
            testDate=temperature.gettestDate(), temperature=temperature.gettemperature(),
            pulse=temperature.getpulse(), breathe=temperature.getbreathe(),shit=temperature.getshit(),
        inWater=temperature.getinWater(),pee=temperature.getpee(),
            weight=temperature.getweight(),bloodPressure=temperature.getbloodPressure())

        updateTemperatureS2D.setTemperatureBaseValues(
            temperature.getpatientId(),temperature.getTempId())

        return updateTemperatureS2D