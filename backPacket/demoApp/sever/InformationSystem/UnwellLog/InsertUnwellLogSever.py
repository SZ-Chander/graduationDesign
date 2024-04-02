from backPacket.demoApp.dao.InformationSystem.UnwellLog.InsertUnwellLogDao import InsertUnwellLogDao

"""
类名：InsertUnwellLogSever
描述：插入白板留言Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
"""
class InsertUnwellLogSever:

    """
    功能阐述:执行单查询功能Sever层主入口
    @:date 2023/4/27
    @:author 常舜志
    """
    def insertUnwellLog(self,unwellLog):
        try:
            staff = unwellLog.getStatusCode()
            unwellLog.setStatusCode(None)
            autority = staff.getStaffAutority()
            if(unwellLog.getDepartId() not in staff.getDepartCode()):
                raise ValueError("无权访问该科室/病区")
            if(autority <= 1):
                unwellLog.setStatusCode(1)
            elif(autority > 1):
                unwellLog.setStatusCode(0)
            else:
                raise ValueError("系统错误，请联系管理员")
            insertUnwellLogDao = InsertUnwellLogDao()
            retData = insertUnwellLogDao.InsertUnwellLog(unwellLog)
            return retData

        except Exception as e:
            return e