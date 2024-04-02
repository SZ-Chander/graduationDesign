from backPacket.demoApp.dao.InformationSystem.NursingRecord import InsertNursingRecordDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import InsertNursingRecordS2D

"""
类名：insertNursingRecordSever
描述：新增护理记录Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class InsertNursingRecordSever:

    """
    功能阐述:新建护理记录功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def insertNursingRecordSever(self,departNursingRecord):
        try:
            dateStringFormat = "%Y-%m-%d %H:%M:%S"
            dateStringFormat2="%Y%m%d%H%M%S"
            departId = departNursingRecord.getDepartId()
            staff = departNursingRecord.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingRecord.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                # patientId,nursingDate,createDate,userId,
                # nursingWhat,inAndOut,selfCareAssess,nursingRounds

                nursingRecord = departNursingRecord.getNursingList()
                createDate = usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat)
                recordId="R"+nursingRecord.getpatientId()+usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat2)
                departNursingRecord.setRecordId(recordId)
                audit_R=0
                audit_A=0

                # 装载参数进入TO
                insertNursingRecordS2D = InsertNursingRecordS2D.InsertNursingRecordS2D()
                insertNursingRecordS2D.setInsertNursingRecordBaseMess(
                    patientId=nursingRecord.getpatientId(),nursingDate=nursingRecord.getnursingDate(),createDate=createDate,
                    userId=nursingRecord.getuserId(),nursingWhat=nursingRecord.getnursingWhat(),Inwater=nursingRecord.getinwater(),
                    selfCareAssess=nursingRecord.getselfCareAssess(),nursingRounds=nursingRecord.getnursingRounds(),
                    recordId=recordId,audit_R=audit_R,audit_A=audit_A,Outwater=nursingRecord.getoutwater())
                # 调用dao层
                insertNursingRecordDao = InsertNursingRecordDao.InsertNursingRecordDao()
                rowCount = insertNursingRecordDao.insertNursingRecordDao(insertNursingRecordS2D)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def setDepartName(self,depart):
        departMessList = depart.getStaff().getDepart()
        departId = depart.getDepartId()
        for departMess in departMessList:
            if(departId == departMess[0]):
                depart.setDepartName(departMess[1])
                break