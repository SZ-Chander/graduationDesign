from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateWhiteBoardContentDao
描述：更新留言信息功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/24
备注：
"""
class UpdateWhiteBoardContentDao:
    def __init__(self):
        self.executeTable = "Table_WhiteBoardConten"
        self.procedure = "updateWhiteBoardContent"
        self.db = current_app.config['db']

    """
    功能阐述: 更新执行单功能Dao层主入口
    @:date 2023/4/24
    @:author 常舜志
    """
    def updateWhiteBoardContentDao(self,updateContentTOS2D):
        daoFuntionKey = updateContentTOS2D.getDaoFuntionKey()
        if(daoFuntionKey == 1):
            retMess = self.updateKeyDao(updateContentTOS2D)
        elif (daoFuntionKey == 2):
            retMess = self.updateContentDao(updateContentTOS2D)
        else:
            retMess = 0
        return retMess

    def updateKeyDao(self,updateContentTOS2D):
        try:
            valueDict = updateContentTOS2D.getValueDict()
            sqlStr = updateContentTOS2D.getSqlStr()
            fullSqlStr = "update {} {} where contentId=:contentId".format(self.executeTable,sqlStr)
            retData = self.db.engine.execute(text(fullSqlStr), valueDict)
            return retData.rowcount
        except Exception as e:
            return e

    def updateContentDao(self,updateContentTOS2D):
        try:
            fullSqlStr = "CALL {}({})".format(self.procedure,updateContentTOS2D.getSqlStr())
            dataDict = updateContentTOS2D.getValueDict()
            self.db.session.execute(text(fullSqlStr),dataDict)
            self.db.session.commit()
            self.db.session.close()
            return 1
        except Exception as e:
            return e