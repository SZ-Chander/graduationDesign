from backPacket.demoApp.dto import Execute
from flask import current_app
from backPacket.demoApp.tools.usefulTools import UsefulTools
from sqlalchemy import text
"""
类名：InsertWhiteBoardContentDao
描述：新建执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/23
备注：
"""
class InsertWhiteBoardContentDao:
    def __init__(self):
        self.procedure = "InsertWhiteBoardContent"
        self.db = current_app.config['db']

    """
    功能阐述: 插入白板留言信息Dao层主入口
    @:date 2023/4/23
    @:author 常舜志
    """
    def insertWhiteBoardContentDao(self,whiteBoardContent):
        try:
            procedureStr = 'CALL {}("{}","{}","{}",{})'.format(self.procedure,
                                                               whiteBoardContent.getCreatUserId(),
                                                               whiteBoardContent.getDepartId(),
                                                               whiteBoardContent.getContent(),
                                                               whiteBoardContent.getRedMess())
            retData = UsefulTools().procedureExecuteHelper(self.db,procedureStr,None)
        except:
            retData = ValueError("新建白板信息失败，请重试!")
        return retData