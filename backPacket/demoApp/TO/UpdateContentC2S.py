from ..dto.WhiteBoardContent import WhiteBoardContent

class UpdateContentTO:
    def __init__(self):
        self.whiteBoardContent = None
        self.updateModeKey = None
        self.sqlStr = None

    def setWhiteBoardContent(self,whiteBoardContent:WhiteBoardContent):
        self.whiteBoardContent = whiteBoardContent
    def setUpdateModeKey(self,updateModeKey:int):
        self.updateModeKey = updateModeKey
    def setSqlStr(self,sqlStr:str):
        self.sqlStr = sqlStr


    def getWhiteBoardContent(self):
        return self.whiteBoardContent
    def getUpdateModeKey(self):
        return self.updateModeKey
    def getSqlStr(self):
        return self.sqlStr