import datetime

import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：StaffFile
描述：护士信息一览实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：马梓洋
完成时间：2023/4/21
备注：实体类修改后务必进行全流程调试！
"""
dateStringFormat = "%Y-%m-%d %H:%M:%S"
class StaffFile:
    def __init__(self):
        self.userId = None
        self.name = None
        self.userDepartCode = None
        self.departName = None
        self.autority = None
        self.sex = None
        self.birthDate = None
        self.IDnumber = None
        self.address = None
        self.professional = None
        self.education= None
        self.employDate = None
        self.politics=None
        self.departId=None
    def setStaffFile(self,userId,name,userDepartCode,departName,autority,sex,birthDate,IDnumber,
                     address,professional,education,employDate,politics):
        self.userId=userId
        self.name = name
        self.userDepartCode = userDepartCode
        self.departName = departName
        self.autority = autority
        self.sex = sex
        self.birthDate = birthDate
        self.IDnumber = IDnumber
        self.address = address
        self.professional = professional
        self.education = education
        self.employDate= usefulTools.UsefulTools().dateTime2String(employDate,dateStringFormat)
        self.politics=politics

    def getuserId(self):
        return self.userId
    def getname(self):
        return self.name
    def getuserDepartCode(self):
        return self.userDepartCode
    def getdepartName(self):
        return self.departName
    def getautority(self):
        return self.autority
    def getsex(self):
        return self.sex
    def getbirthDate(self):
        return self.birthDate
    def getIDnumber(self):
        return self.IDnumber
    def getaddress(self):
        return self.address
    def getprofessional(self):
        return self.professional
    def geteducation(self):
        return self.education
    def getemployDate(self):
        return self.employDate
    def getpolitics(self):
        return self.politics
    def getdepartId(self):
        return self.departId

    def setUserId(self,userId):
        self.userId=userId
    def setName(self,name):
        self.name=name
    def setUserDepartCode(self,userDepartCode):
        self.userDepartCode=userDepartCode
    def setDepartName(self,departName):
        self.departName=departName
    def setAutority(self,autority):
        self.autority=autority
    def setSex(self,sex):
        self.sex=sex
    def setBirthDate(self,birthDate):
        self.birthDate=birthDate
    def setIDnumber(self,IDnumber):
        self.IDnumber=IDnumber
    def setAddress(self,address):
        self.address=address
    def setProfessional(self,professional):
        self.professional=professional
    def setEducation(self,education):
        self.education = education
    def setEmployDate(self,employDate):
        self.employDate = employDate
    def setPolitics(self,politics):
        self.politics = politics
    def setDepartId(self,departId):
        self.departId=departId