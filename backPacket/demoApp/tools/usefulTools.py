from argon2 import PasswordHasher
from datetime import datetime
import datetime

"""
类名：UsefulTools
描述：常用工具集
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/5
"""
class UsefulTools:
    """
    功能阐述:将datetime格式出参转化为string格式的工具方法
    @:date 2023/4/5
    @:author 常舜志
    """
    def dateTime2String(self,inputDate:datetime,stringFormat:str):
        try:
            return inputDate.strftime(stringFormat)
        except:
            return inputDate
    def string2DateTime(self,inputString:str,stringFormat:str):
        try:
            return datetime.datetime.strptime(inputString,stringFormat)
        except:
            return inputString

    def passWordHasher(self,inputPassWord:str):
        ph = PasswordHasher()
        return ph.hash(inputPassWord)
    def passwordChecker(self,hashedPassWord,unhashPassword):
        ph = PasswordHasher()
        try:
            return ph.verify(hashedPassWord,unhashPassword)
        except:
            raise ValueError("密码错误或无效")
    def procedureExecuteHelper(self,db,procedureStr,selectStr):
        db.session.execute(procedureStr)
        if(selectStr != None):
            retData = list(db.session.execute(selectStr))
        else:
            retData = True
        db.session.commit()
        db.session.close()
        return retData
    def obj2Dict(self,inputObj):
        return inputObj.__dict__
    def null2Time(self,startTime,endTime,startDay,endDay):
        if (startTime == None):
            startTime = (datetime.datetime.now() + datetime.timedelta(days=startDay)).strftime("%Y-%m-%d")
        if (endTime == None):
            endTime = (datetime.datetime.now() + datetime.timedelta(days=endDay)).strftime("%Y-%m-%d")
        return startTime, endTime

    def mandarinDate2Format(self,inputStr:str,tarFormat:str,mFormat:str):
        inputDate = self.string2DateTime(inputStr,mFormat)
        return self.dateTime2String(inputDate,tarFormat)

    def startAndEndTimeMandarin2Format(self,startTime:str,endTime:str,inputFormat:str,mFormat:str):
        if("年" or "月" or "日" in startTime):
            startTime = self.mandarinDate2Format(startTime,inputFormat,mFormat)
        if("年" or "月" or "日" in endTime):
            endTime = self.mandarinDate2Format(endTime,inputFormat,mFormat)
        return startTime,endTime

    def strDictFilter(self,inputStr:str,inputDict:dict):
        try:
            return inputDict[inputStr]
        except:
            return inputStr

# if __name__ == '__main__':
#     usf = UsefulTools()
#     st = "2023年4月25日"
#     et = "2023-4-26"
#     print(usf.startAndEndTimeMandarin2Format(st,et,"%Y-%m-%d %H:%M:%S"))