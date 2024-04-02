class DeleteStaffFileS2D:
    def __init__(self):
        self.userId = None

    # userId,name,sex,birthDate,IDnumber,
    # address,professional,education,employDate,politics
    def setDeleteStaffFileBaseValues(self,userId):#主键字段
        self.userId = userId

    def getDaoDict(self):
        daoDict = {"userId":self.userId}

        return daoDict