from backPacket.demoApp.dao.manageSystem.Audit import UpdateAssessAuditDao
from backPacket.demoApp.TO.manageSystem import UpdateAssessAuditS2D

"""
类名：UpdateAssessAuditSever
描述：审核护理评估功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
"""
class UpdateAssessAuditSever:

    """
    功能阐述:审核护理评估功能Sever层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateAssessAuditSever(self,departNursingAssess,updateKey):
        try:
            departId = departNursingAssess.getDepartId()
            staff = departNursingAssess.getStaff()
            updateNursingAssessTO = self.checkKey(departNursingAssess,updateKey)

            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingAssess.getDepartId() in staff.getDepartCode()):
                updateNursingAssessDao = UpdateAssessAuditDao.UpdateAssessAuditDao()
                rowCount = updateNursingAssessDao.updateAssessAuditDao(updateNursingAssessTO)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingAssess,updateKey):
        updateAssessAuditS2D = UpdateAssessAuditS2D.UpdateAssessAuditS2D()
        nursing = departNursingAssess.getNursingList()

        updateAssessAuditS2D.setUpdateAssessAudit(
            audit_A=nursing.getaudit_A(), auditWhy_A=nursing.getauditWhy_A(),
            updateKey=updateKey)

        updateAssessAuditS2D.setAssessAuditBaseValues(
            nursing.getrecordId())

        return updateAssessAuditS2D