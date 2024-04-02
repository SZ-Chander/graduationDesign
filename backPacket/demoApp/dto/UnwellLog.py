class UnwellLog:
    def __init__(self):
        self.logId = None
        self.createId = None
        self.createName = None
        self.createDate = None
        self.staffId = None
        self.staffName = None
        self.happenTime = None
        self.storyContent = None
        self.statusCode = None
        self.statusTime = None
        self.statusStaffId = None
        self.statusStaffName = None
        self.departId = None
        self.departName = None
        self.storyLevel = None
    def setDepartName(self,departName:str):
        self.departName = departName
    def setCreateName(self,createName:str):
        self.createName = createName
    def setStaffName(self,staffName:str):
        self.staffName = staffName
    def setStatusStaffName(self,statusStaffName:str):
        self.statusStaffName = statusStaffName
    def setStoryLevel(self,storyLevel:int):
        self.storyLevel = storyLevel
    def setLogId(self,logId:str):
        self.logId = logId
    def setCreateId(self,createId:str):
        self.createId = createId
    def setCreateDate(self,createDate:str):
        self.createDate = createDate
    def setStaffId(self,staffId:str):
        self.staffId = staffId
    def setHappenTime(self,happenTime:str):
        self.happenTime = happenTime
    def setStoryContent(self,storyContent:str):
        self.storyContent = storyContent
    def setStatusCode(self,statusCode:int):
        self.statusCode = statusCode
    def setStatusTime(self,statusTime:str):
        self.statusTime = statusTime
    def setStatusStaffId(self,statusStaffId:str):
        self.statusStaffId = statusStaffId
    def setDepartId(self,departId:str):
        self.departId = departId

    def getStatusStaffName(self):
        return self.statusStaffName
    def getStaffName(self):
        return self.staffName
    def getDepartName(self):
        return self.departName
    def getCreateId(self):
        return self.createId
    def getCreateDate(self):
        return self.createDate
    def getStaffId(self):
        return self.staffId
    def getHappenTime(self):
        return self.happenTime
    def getStoryContent(self):
        return self.storyContent
    def getStatusCode(self):
        return self.statusCode
    def getStatusTime(self):
        return self.statusTime
    def getStatusStaffId(self):
        return self.statusStaffId
    def getDepartId(self):
        return self.departId
    def getLogId(self):
        return self.logId
    def getStoryLevel(self):
        return self.storyLevel
