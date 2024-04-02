from backPacket.demoApp.dao.manageSystem.Audit import UpdateTempAuditDao
from backPacket.demoApp.TO.manageSystem import UpdateTempAuditS2D

"""
类名：UpdateTempAuditSever
描述：审核体温单功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/25
"""
class UpdateTempAuditSever:

    """
    功能阐述:审核体温单功能Sever层主入口
    @:date 2023/4/25
    @:author 马梓洋
    """
    def updateTempAuditSever(self,departNursingTemp,updateKey):
        try:
            departId = departNursingTemp.getDepartId()
            staff = departNursingTemp.getStaff()
            updateNursingTempTO = self.checkKey(departNursingTemp,updateKey)

            if(departId == None):
                raise ValueError("departId不能为空")
            if(departNursingTemp.getDepartId() in staff.getDepartCode()):
                updateNursingTempDao = UpdateTempAuditDao.UpdateTempAuditDao()
                rowCount = updateNursingTempDao.updateTempAuditDao(updateNursingTempTO)
                if(rowCount >0):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departNursingTemp,updateKey):
        updateTempAuditS2D = UpdateTempAuditS2D.UpdateTempAuditS2D()
        nursing = departNursingTemp.getNursingList()

        updateTempAuditS2D.setUpdateTempAudit(
            audit=nursing.getaudit(), auditWhy=nursing.getauditWhy(),
            updateKey=updateKey)

        updateTempAuditS2D.setTempAuditBaseValues(
            nursing.getTempTableId())

        return updateTempAuditS2D