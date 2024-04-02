from backPacket.demoApp.dao.InformationSystem.NursingAssess import InsertNursingAssessDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import InsertNursingAssessS2D

"""
类名：insertNursingAssessSever
描述：新增护理评估Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class InsertNursingAssessSever:

    """
    功能阐述:新建护理记录功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def insertNursingAssessSever(self,departNursingAssess):
        try:
            dateStringFormat = "%Y-%m-%d %H:%M:%S"
            dateStringFormat2="%Y%m%d%H%M%S"
            departId = departNursingAssess.getDepartId()
            staff = departNursingAssess.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingAssess.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                # patientId,nursingDate,createDate,userId,
                # nursingWhat,inAndOut,selfCareAssess,nursingRounds

                nursingAssess = departNursingAssess.getNursingList()
                createDate = usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat)
                recordId=departNursingAssess.getrecordId()
                lastUpDate=createDate

                # 装载参数进入TO
                insertNursingAssessS2D = InsertNursingAssessS2D.InsertNursingAssessS2D()
                insertNursingAssessS2D.setInsertNursingAssessBaseMess(
                    patientId=nursingAssess.getpatientId(),lastUpDate=lastUpDate,createDate=createDate,
                    userId=nursingAssess.getuserId(),recordId=recordId,audit=0)
                # 调用dao层
                insertNursingAssessDao = InsertNursingAssessDao.InsertNursingAssessDao()
                rowCount = insertNursingAssessDao.insertNursingAssessDao(insertNursingAssessS2D)
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