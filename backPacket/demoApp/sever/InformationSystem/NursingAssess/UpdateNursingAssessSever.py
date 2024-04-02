from backPacket.demoApp.dao.InformationSystem.NursingAssess import UpdateNursingAssessDao
from backPacket.demoApp.TO import UpdateNursingAssessS2D
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
"""
类名：UpdateNursingAssessSever
描述：更新护理评估功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class UpdateNursingAssessSever:

    """
    功能阐述:更新护理评估功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def updateNursingAssessSever(self,departNursingAssess):
        try:

            departId = departNursingAssess.getDepartId()
            staff = departNursingAssess.getStaff()
            key = self.checkKey(departNursingAssess)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingAssess.getDepartId() in staff.getDepartCode()):
                updateNursingAssessDao = UpdateNursingAssessDao.UpdateNursingAssessDao()
                rowCount = updateNursingAssessDao.updateNursingAssessDao(key)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingAssess):
        dateStringFormat = "%Y-%m-%d %H:%M:%S"
        dateStringFormat2="%Y%m%d%H%M%S"
        updateNursingAssessS2D = UpdateNursingAssessS2D.UpdateNursingAssessS2D()
        nursing = departNursingAssess.getNursingList()
        lastUpDate= usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),dateStringFormat)

        #lastUpDate,allergy,conscious,position,communication,limb,
        #swallow,eyes,food,shit,pee,chronic
        updateNursingAssessS2D.setUpdateNursingAssess(
            nursingAssess=nursing.getnursingAssess(),lastUpDate=lastUpDate,allergy=nursing.getallergy(),conscious=nursing.getconscious(),
            position=nursing.getposition(),communication=nursing.getcommunication(),limb=nursing.getlimb(),swallow=nursing.getswallow(),
            eyes=nursing.geteyes(),food=nursing.getfood(),shit=nursing.getshit(),pee=nursing.getpee(),chronic=nursing.getchronic(),userId=nursing.getuserId()
        )
        #patientId,userId,createDate
        updateNursingAssessS2D.setNursingAssessBaseValues(
            nursing.getrecordId())

        return updateNursingAssessS2D