class WhiteBoard:
    def __init__(self):
        self.staff = None
        self.departId = None
        self.workingStaffNameList = None
        self.workingStaffNum = None
        self.totoalBedNum = None
        self.usedBedNum = None
        self.outPatientNum = None
        self.inPatientNum = None
        self.listContent = None
        self.staffListStr = None
    def setStaffListStr(self,staffListStr:str):
        self.staffListStr = staffListStr
    def setListContent(self,listContent):
        self.listContent = listContent
    def setOutPatientNum(self,outPatientNum):
        self.outPatientNum = outPatientNum
    def setInPatientNum(self,inPatientNum):
        self.inPatientNum = inPatientNum
    def setUsedBedNum(self,usedBedNum):
        self.usedBedNum = usedBedNum
    def setTotoalBedNum(self,totoalBedNum):
        self.totoalBedNum = totoalBedNum
    def setWorkingStaffNum(self,workingStaffNum):
        self.workingStaffNum = workingStaffNum
    def setWorkingStaffNameList(self,workingStaffNameList):
        self.workingStaffNameList = workingStaffNameList
    def setStaff(self,staff):
        self.staff = staff
    def setDepartId(self,departId):
        self.departId = departId
    def setTotalBedNumByStr(self,totalBedStr,splitKey):
        totalBedStrList = totalBedStr.split(splitKey)
        baseNum = int(totalBedStrList[0])
        self.totoalBedNum = baseNum + len(totalBedStrList) - 1
    def setWorkingStaffNameListByStr(self,nameListStr,splitKey):
        if(nameListStr != None):
            self.workingStaffNameList = nameListStr.split(splitKey)
        else:
            self.workingStaffNameList = "未查到排班信息"
    def getWorkingStaffNameList(self):
        return self.workingStaffNameList
    def getStaffListStr(self):
        return self.staffListStr
    def getDataDict(self):
        dataDict = {'staff':self.staff.__dict__,
                    'departId':self.departId} #基础信息
        dataDict['totoalBedNum'] = self.totoalBedNum #总床位数
        dataDict['usedBedNum'] = self.usedBedNum #已用床位数
        dataDict['bedUseRate'] = "{:.2f}%".format((self.usedBedNum/self.totoalBedNum)*100)#当前床位占用率
        dataDict['todayInPatientNum'] = str(self.inPatientNum) #今日出科
        dataDict['todayOutPatientNum'] = str(self.outPatientNum) #今日入科
        dataDict['workingStaffList'] = self.workingStaffNameList #当前在班工作人员
        dataDict['workingStaffNum'] = self.workingStaffNum #当前在班工作人员数量
        dataDict['listContent'] = []
        for line in self.listContent:
            dataDict['listContent'].append(line.__dict__)
        dataDict['staffListStr'] = self.staffListStr
        return dataDict
