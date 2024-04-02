from ..dto.Staff import Staff
class UnwellVo:
    def __init__(self):
        self.logId = None
        self.staffName = None
        self.happenTime = None
        self.storyContent = None
        self.statusCode = None
        self.statusTime = None
        self.statusStaffName = None
        self.storyLevel = None
        self.departName = None
    def setUnwellVofromDto(self,unwellDto):
        self.logId = unwellDto.getLogId()
        self.staffName = unwellDto.getStaffName()
        self.happenTime = unwellDto.getHappenTime().strftime("%Y年%m月%d日 %H:%M:%S")
        self.storyContent = unwellDto.getStoryContent()
        self.statusCode = unwellDto.getStatusCode()
        self.statusTime = unwellDto.getStatusTime().strftime("%Y年%m月%d日 %H:%M:%S")
        self.statusStaffName = unwellDto.getStatusStaffName()
        self.storyLevel = unwellDto.getStoryLevel()
        self.departName = unwellDto.getDepartName()
        self.departName = unwellDto.getDepartName()
    def transKey(self):
        statusCodeDict = {0:"未审核",1:"护士长审核完成",2:"护理部审核完毕"}
        storyLevelDict = {1:"一级事件",2:"二级事件",3:"三级事件",4:"四级事件"}
        self.statusCode = statusCodeDict[self.statusCode]
        self.storyLevel = storyLevelDict[self.storyLevel]