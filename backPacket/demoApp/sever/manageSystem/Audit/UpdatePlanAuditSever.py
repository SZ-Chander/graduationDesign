from backPacket.demoApp.dao.manageSystem.Audit import UpdatePlanAuditDao
from backPacket.demoApp.TO.manageSystem import UpdatePlanAuditS2D

"""
类名：UpdatePlanAuditSever
描述：审核护理计划功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/24
"""
class UpdatePlanAuditSever:

    """
    功能阐述:审核护理计划功能Sever层主入口
    @:date 2023/4/24
    @:author 马梓洋
    """
    def updatePlanAuditSever(self,departNursingPlan,updateKey):
        try:
            departId = departNursingPlan.getDepartId()
            staff = departNursingPlan.getStaff()
            updateNursingPlanTO = self.checkKey(departNursingPlan,updateKey)

            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingPlan.getDepartId() in staff.getDepartCode()):
                updateNursingPlanDao = UpdatePlanAuditDao.UpdatePlanAuditDao()
                rowCount = updateNursingPlanDao.updatePlanAuditDao(updateNursingPlanTO)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingPlan,updateKey):
        updatePlanAuditS2D = UpdatePlanAuditS2D.UpdatePlanAuditS2D()
        nursing = departNursingPlan.getNursingList()

        updatePlanAuditS2D.setUpdatePlanAudit(
            audit=nursing.getaudit(), auditWhy=nursing.getauditWhy(),
            updateKey=updateKey)

        updatePlanAuditS2D.setPlanAuditBaseValues(
            nursing.getplanId())

        return updatePlanAuditS2D