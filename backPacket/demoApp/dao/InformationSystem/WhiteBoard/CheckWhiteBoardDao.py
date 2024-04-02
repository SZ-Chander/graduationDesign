from flask import current_app
from sqlalchemy import text
from backPacket.demoApp.dto import WhiteBoardContent
"""
类名：CheckWhiteBoardDao
描述：查询护理白板数据功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/15
备注：
"""
class CheckWhiteBoardDao:
    def __init__(self):
        self.procedure = "GetWhiteBoardData"
        self.contentTable = "View_WhiteBoardConten"
        self.db = current_app.config['db']

    """
    功能阐述: 查询护理白板信息Dao层主入口
    @:date 2023/4/15
    @:author 常舜志
    """
    def checkWhiteBoardDao(self,whiteBoardRoutines):
        # 通过存储过程读取白板信息
        self.db.session.execute('CALL {}("{}", @out_bedDict, @out_usingBedCount, @out_enterPatientCount, @out_outPatientCount, @out_workingStaffName, @out_workingStaffCount)'.format(self.procedure,whiteBoardRoutines.getDepartId()))
        retData = self.db.session.execute('SELECT @out_bedDict, @out_usingBedCount, @out_enterPatientCount, @out_outPatientCount, @out_workingStaffName, @out_workingStaffCount').fetchall()
        usefulData = retData[0]
        self.db.session.close()
        # 存储过程读取完毕，开始装载科室信息
        whiteBoardRoutines.setWhiteBoardRoutines(usefulData[0], usefulData[1], usefulData[2], usefulData[3],
                                                 usefulData[4], usefulData[5])
        # 科室信息装载完毕，开始读取白板留言信息
        sqlStr = "select editUserName,editDate,content,redMess,topMess,contentId from {} where departId=:departId and visibleKey=1 and (editDate between :startTime and :endTime or topMess=1)".format(self.contentTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=whiteBoardRoutines.getDepartId(),startTime=whiteBoardRoutines.getStartTime(),endTime=whiteBoardRoutines.getEndTime())))
        # 留言信息读取完毕，开始装载留言信息
        listContents = []
        for dataLine in retData:
            whiteBoardContent = WhiteBoardContent.WhiteBoardContent()
            whiteBoardContent.setContent(dataLine[0],dataLine[1],dataLine[2],dataLine[3])
            whiteBoardContent.setTopMess(dataLine[4])
            whiteBoardContent.setContentId(dataLine[5])
            listContents.append(whiteBoardContent)
        return whiteBoardRoutines,listContents