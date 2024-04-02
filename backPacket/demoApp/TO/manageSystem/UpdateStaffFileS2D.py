class UpdateStaffFileS2D:
    def __init__(self):
        self.userId = None
        self.name = None

        self.sex=None
        self.birthDate = None
        self.IDnumber = None
        self.address = None
        self.professional = None
        self.education = None
        self.employDate = None
        self.politics = None


# userId,name,sex,birthDate,IDnumber,
# address,professional,education,employDate,politics
    def setUpdateStaffFile(self,name,sex,birthDate,IDnumber,
                            address,professional,education,employDate,politics):#设置需要更新的字段

        self.name = name

        self.sex=sex
        self.birthDate = birthDate
        self.IDnumber = IDnumber
        self.address = address
        self.professional = professional
        self.education = education
        self.employDate = employDate
        self.politics = politics

    def setStaffFileBaseValues(self,userId):#主键字段
        self.userId = userId

    def getDaoDict(self):
        daoDict = {"userId":self.userId}
        daoDict["sex"] = self.sex
        daoDict["birthDate"] = self.birthDate
        daoDict["IDnumber"] = self.IDnumber
        daoDict["address"] = self.address
        daoDict["professional"] = self.professional
        daoDict["education"] = self.education
        daoDict["employDate"] = self.employDate
        daoDict["politics"] = self.politics
        return daoDict

    def getDaoDict2(self):
        daoDict = {"userId":self.userId}
        daoDict["name"] = self.name
        return daoDict

    def getSqlValues(self):
        return "sex=:sex,birthDate=:birthDate,IDnumber=:IDnumber,address=:address,professional=:professional,education=:education,employDate=:employDate,politics=:politics"

    def getSqlValues2(self):
        return "name=:name"