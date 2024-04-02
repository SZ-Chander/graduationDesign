from backPacket.demoApp.dao.InformationSystem.WorkSchedule.CheckWorkScheduleDao import CheckWorkScheduleDao
from backPacket.demoApp.dto.WorkSchedulePage import WorkSchedulePage
"""
类名：CheckWorkScheduleSever
描述：获取护理白板信息Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/13
"""
class CheckWorkScheduleSever:

    """
    功能阐述:护理白板信息查询功能Sever层主入口
    @:date 2023/4/12
    @:author 常舜志
    """
    def CheckWorkSchedule(self,workSchedule,staff):
        try:
            if(workSchedule.getWorkStaffId() != staff.getStaffId()):
                raise ValueError("系统错误，请联系管理员")
            checkWorkScheduleDao = CheckWorkScheduleDao()
            workSchedulePage = checkWorkScheduleDao.checkWorkSchedule(workSchedule)
            if(workSchedulePage.__class__ == WorkSchedulePage):
                workSchedulePage.setStaff(staff)
                workSchedulePage.setWorkScheduleList(list(map(self.viewObj2Dict,workSchedulePage.getWorkScheduleList())))
                workSchedulePage.setStaff(workSchedulePage.staff.__dict__)
                return workSchedulePage.__dict__
            else:
                return workSchedulePage

        except Exception as e:
            return e

    def viewObj2Dict(self,workSchedule_View):
        return dict(startTime=workSchedule_View.getStartTime(),endTime=workSchedule_View.getEndTime(),
                    editTime=workSchedule_View.getEditTime(),createStaffName=workSchedule_View.getCreateStaffName(),
                    workStaffName=workSchedule_View.getWorkStaffName(),workDepartName=workSchedule_View.getWorkDepartName(),
                    workId=workSchedule_View.getWorkId())