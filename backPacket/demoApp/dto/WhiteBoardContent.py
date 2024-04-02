class WhiteBoardContent:
    def __init__(self):
        self.editUserName = None
        self.editDate = None
        self.content = None
        self.redMess = None

        self.creatUserId = None
        self.creatUserName = None
        self.creatDate = None
        self.editUserId = None
        self.departId = None
        self.departName = None
        self.content = None
        self.visibleKey = None
        self.topMess = None
        self.redMess = None
        self.contentId = None

    def setContent(self,editUserName,editDate,content,redMess):
        self.editUserName = editUserName
        self.editDate = editDate.strftime("%Y年%m月%d日 %H:%M:%S")
        self.content = content
        self.redMess = redMess

    def setContentId(self,contentId:str):
        self.contentId = contentId
    def setDepartId(self,departId):
        self.departId = departId
    def setCreateUserId(self,creatUserId):
        self.creatUserId = creatUserId
    def setContents(self,content):
        self.content = content
    def setRedMess(self,redMess):
        self.redMess = redMess
    def setTopMess(self,topMess):
        self.topMess = topMess
    def setCreatDate(self,creatDate):
        self.creatDate = creatDate
    def setVisibleKey(self,visibleKey):
        self.visibleKey = visibleKey
    def setEditUserId(self,editUserId):
        self.editUserId = editUserId

    def getDepartId(self):
        return self.departId
    def getContentId(self):
        return self.contentId
    def getCreatUserId(self):
        return self.creatUserId
    def getContent(self):
        return self.content
    def getRedMess(self):
        return self.redMess
    def getTopMess(self):
        return self.topMess
    def getCreatDate(self):
        return self.creatDate
    def getVisibleKey(self):
        return self.visibleKey
    def getEditUserId(self):
        return self.editUserId