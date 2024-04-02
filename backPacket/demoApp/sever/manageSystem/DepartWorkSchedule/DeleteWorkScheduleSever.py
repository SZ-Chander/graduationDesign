from datetime import datetime
from backPacket.demoApp.dao.manageSystem.DepartWorkSchedule.DeleteWorkScheduleDao import DeleteWorkScheduleDao
from backPacket.demoApp.tools.usefulTools import UsefulTools
"""
类名：DeleteWorkScheduleSever
描述：创建新账号功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/28
"""
class DeleteWorkSchedule:

    """
    功能阐述:新建排班信息Sever层主入口
    @:date 2023/4/28
    @:author 常舜志
    """
    def deleteWorkSchedule(self,workSchedule):
        try:
            staff = workSchedule.getStaff()
            workStaffDepartId = workSchedule.getWorkStaffDepart()
            endTimeDate = UsefulTools().string2DateTime(workSchedule.getEndTime(),"%Y-%m-%d %H:%M:%S")
            if(type(endTimeDate) != datetime):
                raise ValueError("时间格式错误，请联系管理员！")
            if(workStaffDepartId in staff.getDepartCode()):
                if(staff.getStaffAutority() > 1):
                    raise ValueError("您无权进行该操作！")
                if(endTimeDate < datetime.now()):
                    raise ValueError("您不能删除已经结束的排班！")
                deleteWorkScheduleDao = DeleteWorkScheduleDao()
                retData = deleteWorkScheduleDao.deleteWorkSchedule(workSchedule)

                if(retData == 1):
                    return "删除排班信息成功！"
                elif(retData == -10):
                    raise ValueError("系统错误，请检查数据")
                else:
                    raise ValueError("系统错误，请联系管理员\nCode：1145")
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e