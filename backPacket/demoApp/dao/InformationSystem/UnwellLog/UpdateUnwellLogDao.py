from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：UpdateUnwellDao
描述：查询执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/4
备注：
"""
class UpdateUnwellDao:
    def __init__(self):
        self.executeTable = "Table_Unwell_Log"
        self.db = current_app.config['db']

    """
    功能阐述: 更新执行单功能Dao层主入口
    @:date 2023/4/4
    @:author 常舜志
    """
    def updateUnwellDao(self,unwellLog):
        storyContent = unwellLog.getStoryContent()
        logId = unwellLog.getLogId()
        sqlStr = "update {} SET storyContent=:storyContent where logId=:logId".format(self.executeTable)
        retData = self.db.engine.execute(text(sqlStr),dict(storyContent=storyContent,logId=logId))
        return retData.rowcount