from backPacket.demoApp.dao.InformationSystem.NursingRecord import UpdateNursingRecordDao
from backPacket.demoApp.TO import UpdateNursingRecordS2D

"""
类名：UpdateNursingRecordSever
描述：更新护理记录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class UpdateNursingRecordSever:

    """
    功能阐述:更新护理记录功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def updateNursingRecordSever(self,departNursingRecord):
        try:
            departId = departNursingRecord.getDepartId()
            staff = departNursingRecord.getStaff()
            key = self.checkKey(departNursingRecord)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingRecord.getDepartId() in staff.getDepartCode()):
                updateNursingRecordDao = UpdateNursingRecordDao.UpdateNursingRecordDao()
                rowCount = updateNursingRecordDao.updateNursingRecordDao(key)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingRecord):
        updateNursingRecordS2D = UpdateNursingRecordS2D.UpdateNursingRecordS2D()
        nursing = departNursingRecord.getNursingList()


#nursingDate,nursingWhat,inAndOut,selfCareAssess,nursingRounds
        updateNursingRecordS2D.setUpdateNursingRecord(
            nursingDate=nursing.getnursingDate(), nursingWhat=nursing.getnursingWhat(),
            Inwater= nursing.getinwater(), selfCareAssess=nursing.getselfCareAssess(),
            nursingRounds=nursing.getnursingRounds(),Outwater=nursing.getoutwater())
#patientId,userId,createDater
        updateNursingRecordS2D.setNursingRecordBaseValues(
            nursing.getrecordId())

        return updateNursingRecordS2D