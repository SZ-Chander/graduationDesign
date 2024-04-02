from flask import current_app
from sqlalchemy import text
"""
类名：UpdateUnwellDao
描述：查询执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/5/1
备注：
"""
class UpdateUnwellManageDao:
    def __init__(self):
        self.executeTable = "Table_Unwell_Log"
        self.db = current_app.config['db']

    """
    功能阐述: 更新执行单功能Dao层主入口
    @:date 2023/5/1
    @:author 常舜志
    """
    def updateUnwellManage(self,unwellLog):
        storyContent = unwellLog.getStoryContent()
        logId = unwellLog.getLogId()
        statusCode = unwellLog.getStatusCode()
        storyLevel = unwellLog.getStoryLevel()
        modeKey = unwellLog.getCreateId()
        if(modeKey == 1):# 审批模式
            sqlStr = "update {} SET statusCode=:statusCode where logId=:logId".format(self.executeTable)
            dataDict = dict(statusCode=statusCode,logId=logId)
        elif(modeKey == 0):# 修改信息模式:
            sqlStr = "update {} SET storyContent=:storyContent, storyLevel=:storyLevel where logId=:logId".format(self.executeTable)
            dataDict = dict(storyContent=storyContent,storyLevel=storyLevel,logId=logId)
        else:
            raise ValueError("系统错误，请联系管理员！")
        retData = self.db.engine.execute(text(sqlStr),dataDict)
        return retData.rowcount