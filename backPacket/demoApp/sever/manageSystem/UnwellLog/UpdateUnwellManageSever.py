from backPacket.demoApp.dao.manageSystem.UnwellLog.UpdateUnwellManageDao import UpdateUnwellManageDao

"""
类名：UpdateUnwellManageSever
描述：更新不良事件Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/5/1
"""
class UpdateUnwellManageSever:

    """
    功能阐述:更新不良事件功能Sever层主入口
    @:date 2023/5/1
    @:author 常舜志
    """
    def updateUnwellManage(self,unwellLog,staff,newStatusCode):
        try:
            departId = unwellLog.getDepartId()
            if(unwellLog.getStatusCode() > 1):
                raise ValueError("该信息已由护理部审核，无法修改！")
            else:
                unwellLog.setStatusCode(newStatusCode)
            if(departId not in staff.getDepartCode()):
                raise ValueError("您只能修改本科室的数据！")
            if(unwellLog.getStatusCode() > 1):
                raise ValueError("系统错误，请联系管理员！")
            updateUnwellDao = UpdateUnwellManageDao()
            retData = updateUnwellDao.updateUnwellManage(unwellLog)
            if(retData != 1):
                raise ValueError("修改失败，请检查数据或联系管理员")
            else:
                return "修改成功！"
        except Exception as e:
            return e