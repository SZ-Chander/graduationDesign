class InsertStaffFileS2D:
    def __init__(self):
        self.userId = None
        self.sex=None
        self.birthDate = None
        self.IDnumber = None
        self.address = None
        self.professional = None
        self.education = None
        self.employDate = None
        self.politics = None
        # userId,sex,birthDate,IDnumber,
    # address,professional,education,employDate,politics

    def setInsertStaffFileBaseMess(self,userId,sex,birthDate,IDnumber,
                                       address,professional,education,employDate,politics):
        self.userId = str(userId)

        self.sex = str(sex)
        self.birthDate = birthDate
        self.IDnumber = str(IDnumber)
        self.address = str(address)
        self.professional = str(professional)
        self.education = str(education)
        self.employDate = employDate
        self.politics = str(politics)

    def getDaoDict(self):
        daoDict = {"userId":self.userId}
        return daoDict
    def getSqlValuesStr(self):
        return ":userId,:sex,:birthDate,:IDnumber,:address,:professional,:education,:employDate,:politics"
    def getSqlFormatStr(self):
        return "userId,sex,birthDate,IDnumber,address,professional,education,employDate,politics"