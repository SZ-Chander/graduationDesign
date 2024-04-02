from backPacket.demoApp.dao.InformationSystem.Execute import UpdateExecuteDao
from backPacket.demoApp.TO import UpdateExecuteS2D

"""
类名：UpdateExecuteSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/4
"""
class UpdateExecuteSever:

    """
    功能阐述:更新执行单功能Sever层主入口
    @:date 2023/4/4
    @:author 常舜志
    """
    def updateExecuteSever(self,departExecute,updateKey):
        try:
            departId = departExecute.getDepartId()
            staff = departExecute.getStaff()
            key, updateExecuteTO = self.checkKey(departExecute,updateKey)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departExecute.getDepartId() in staff.getDepartCode()):
                updateExecuteDao = UpdateExecuteDao.UpdateExecuteDao()
                rowCount = updateExecuteDao.updateExecuteDao(updateExecuteTO)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departExecute,updateKey):
        updateExecuteS2D = UpdateExecuteS2D.UpdateExecuteS2D()
        execute = departExecute.getExecuteList()
        keyExecuteTime = (execute.getExecuteTime() is not None)
        keyExecuteKey = (execute.getExecuteKey() == 0)
        keyCompleteDate = (execute.getCompleteDate() is not None)
        keyCompleteKey = (execute.getCompleteKey() == 0)
        retKey = False
        checkExecuteValue = keyExecuteTime & keyExecuteKey
        checkCompleteValue = keyCompleteKey & keyCompleteDate
        if(updateKey == 1):
            retKey = checkExecuteValue
        if(updateKey == 2):
            retKey = checkCompleteValue
        if(updateKey == 3):
            retKey = checkExecuteValue & checkCompleteValue
        updateExecuteS2D.setUpdateExecute(executeKey=execute.getExecuteKey(), executeTime=execute.getExecuteTime(),
                                          completeKey=execute.getCompleteKey(), completeDate=execute.getCompleteDate(),
                                          updateKey=updateKey)
        updateExecuteS2D.setExecuteBaseValues(execute.getPatientId(),execute.getvisitId(),execute.getExecuteId(),execute.getExecuteSubId(),execute.getExecuteLabel())
        return retKey, updateExecuteS2D