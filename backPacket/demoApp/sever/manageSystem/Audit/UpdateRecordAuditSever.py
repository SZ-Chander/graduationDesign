from backPacket.demoApp.dao.manageSystem.Audit import UpdateRecordAuditDao
from backPacket.demoApp.TO.manageSystem import UpdateRecordAuditS2D

"""
类名：UpdateRecordAuditSever
描述：审核护理记录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
"""
class UpdateRecordAuditSever:

    """
    功能阐述:审核护理记录功能Sever层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateRecordAuditSever(self,departNursingRecord,updateKey):
        try:
            departId = departNursingRecord.getDepartId()
            staff = departNursingRecord.getStaff()
            updateNursingRecordTO = self.checkKey(departNursingRecord,updateKey)

            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingRecord.getDepartId() in staff.getDepartCode()):
                updateNursingRecordDao = UpdateRecordAuditDao.UpdateRecordAuditDao()
                rowCount = updateNursingRecordDao.updateRecordAuditDao(updateNursingRecordTO)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingRecord,updateKey):
        updateRecordAuditS2D = UpdateRecordAuditS2D.UpdateRecordAuditS2D()
        nursing = departNursingRecord.getNursingList()

        updateRecordAuditS2D.setUpdateRecordAudit(
            audit_R=nursing.getaudit_R(), auditWhy_R=nursing.getauditWhy_R(),
            updateKey=updateKey)

        updateRecordAuditS2D.setRecordAuditBaseValues(
            nursing.getrecordId())

        return updateRecordAuditS2D