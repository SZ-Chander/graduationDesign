from backPacket.demoApp.dao.InformationSystem.NursingPlan import UpdateNursingPlanDao
from backPacket.demoApp.TO import UpdateNursingPlanS2D

"""
类名：UpdateNursingPlanSever
描述：更新护理计划功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/6
"""
class UpdateNursingPlanSever:

    """
    功能阐述:更新护理计划功能Sever层主入口
    @:date 2023/4/6
    @:author 马梓洋
    """
    def updateNursingPlanSever(self,departNursingPlan,updateKey):
        try:
            departId = departNursingPlan.getDepartId()
            staff = departNursingPlan.getStaff()
            updateNursingPlanTO = self.checkKey(departNursingPlan,updateKey)
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingPlan.getDepartId() in staff.getDepartCode()):
                updateNursingPlanDao = UpdateNursingPlanDao.UpdateNursingPlanDao()
                rowCount = updateNursingPlanDao.updateNursingPlanDao(updateNursingPlanTO)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingPlan,updateKey):
        updateNursingPlanS2D = UpdateNursingPlanS2D.UpdateNursingPlanS2D()
        nursing = departNursingPlan.getNursingList()

        updateNursingPlanS2D.setUpdateNursingPlan(
            lastUpdateDate=nursing.getlastUpdateDate(), planStatus=nursing.getplanStatus(),
          updateKey= updateKey, stopDate=nursing.getstopDate(),stopUser=nursing.getstopUser(),stopWhy=nursing.getstopWhy(),
        nursingPlan=nursing.getnursingPlan())

        updateNursingPlanS2D.setNursingPlanBaseValues(
            nursing.getplanId())

        return updateNursingPlanS2D