import datetime

import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：TempTable
描述：创建体温单实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/5/2
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class TempTable:
    def __init__(self):


        self.TempId=None
        self.TempTableId=None
        self.TempIdList=[]
        self.times=None
    def getTempId(self):
        return self.TempId
    def gettimes(self):
        return self.times
    def getTempIdList(self):
        return self.TempIdList

    def setTempIdList(self,TempId):
        self.TempIdList.append(TempId)
    def setTimes(self,times):
        self.times=times
    def setTempId(self,TempId):
        self.TempId=TempId
