from flask import current_app
from sqlalchemy import text
from backPacket.demoApp.dto.UnwellLog import UnwellLog
"""
类名：CheckUnwellDao
描述：查询执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/26
备注：
"""
class CheckUnwellDao:
    def __init__(self):
        self.executeMessTable = "View_Unwell_Log"
        self.db = current_app.config['db']

    """
    功能阐述: 查询执行单功能Dao层主入口
    @:date 2023/4/26
    @:author 常舜志
    """
    def checkUnwellDao(self,unwellLogPage):
        # 读取dto信息并生成sql字符串
        sqlStr = "select logId,staffName,happenTime,storyContent,statusCode,statusTime,statusStaffName,storyLevel,departName from {} where departId=:departId and createDate between :startTime and :endTime".format(self.executeMessTable)
        # 执行sql字符串
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=unwellLogPage.getDepartId(),startTime=unwellLogPage.getStartTime(),endTime=unwellLogPage.getEndTime())))
        # 将返回的信息装载进DTO
        executeList = []
        if(len(retData) == 0):
            pass
        else:
            unwellLogPage.setDepartName(retData[0][8])
            for dataLine in retData:
                unwellLog = UnwellLog()
                unwellLog.setLogId(dataLine[0])
                unwellLog.setStaffName(dataLine[1])
                unwellLog.setHappenTime(dataLine[2])
                unwellLog.setStoryContent(dataLine[3])
                unwellLog.setStatusCode(dataLine[4])
                unwellLog.setStatusTime(dataLine[5])
                unwellLog.setStatusStaffName(dataLine[6])
                unwellLog.setStoryLevel(dataLine[7])
                unwellLog.setDepartName(dataLine[8])
                executeList.append(unwellLog)
        unwellLogPage.setUnwellLogList(executeList)
        return unwellLogPage