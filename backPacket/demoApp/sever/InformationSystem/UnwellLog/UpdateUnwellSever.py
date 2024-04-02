from backPacket.demoApp.dao.InformationSystem.UnwellLog.UpdateUnwellLogDao import UpdateUnwellDao

"""
类名：UpdateUnwellSever
描述：更新不良事件Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
"""
class UpdateUnwellSever:

    """
    功能阐述:更新不良事件功能Sever层主入口
    @:date 2023/4/27
    @:author 常舜志
    """
    def updateUnwellSever(self,unwellLog):
        try:
            userId = unwellLog.getStaffId()
            logId = unwellLog.getLogId()
            userLogId = logId.split("T")[0].replace("UWU","")
            statusCode = unwellLog.getStatusCode()
            if(userId != userLogId):
                raise ValueError("您只能修改您创建的不良事件报告!\n若您是管理员，请使用管理员端修改他人不良事件报告！")
            if(statusCode > 0):
                raise ValueError("您只能修改未审核状态的不良事件报告！\n若您是管理员，请使用管理员端修改不良事件报告！")
            updateUnwellDao = UpdateUnwellDao()
            retData = updateUnwellDao.updateUnwellDao(unwellLog)
            if(retData != 1):
                raise ValueError("修改失败，请检查数据或联系管理员")
            else:
                return "修改成功！"
        except Exception as e:
            return e