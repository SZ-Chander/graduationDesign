from backPacket.demoApp.dto import NursingRecord
from flask import current_app
from sqlalchemy import text
"""
类名：NursingRecordDao
描述：护理记录Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/1
备注：
"""
class NursingRecordDao:
    def __init__(self):
        self.nursingRecordTable = "View_inNursingRecord"
        self.db = current_app.config['db']

    """
    功能阐述: 护理记录Dao层主入口
    @:date 2023/3/30
    @:author 马梓洋
    """
    def nursingRecordDao(self,depart):

        sqlStr = "select * from {} where departId=:departId and createDate BETWEEN :BeginDate AND :EndDate".format(self.nursingRecordTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId(),BeginDate=depart.getBeginDate(),EndDate=depart.getEndDate())))

        recordList = []
        for nursingRecord in retData:
            record = NursingRecord.NursingRecord()
            record.setNursingRecord(
                patientName=nursingRecord[0],patientAge=nursingRecord[1],departId=nursingRecord[2],departName=nursingRecord[3],createDate=nursingRecord[4],
                nursingDate=nursingRecord[5],userName=nursingRecord[6],nursingWhat=nursingRecord[7],Inwater=nursingRecord[8],selfCareAssess=nursingRecord[9],
                nursingRounds=nursingRecord[10],Outwater=nursingRecord[11],recordId=nursingRecord[12],audit_R=nursingRecord[13],
                auditWhy_R=nursingRecord[14],patientId=nursingRecord[15]
            )
            recordList.append(record)
        depart.setNursingList(recordList)
        return depart