from backPacket.demoApp.dao.manageSystem.DepartWorkSchedule.CheckDepartWorkSchedulePageDao import CheckDepartWorkSchedulePageDao
from backPacket.demoApp.VO.manageSystem.DepartWorkSchedulePageVO import DepartWorkSchedulePageVO
from backPacket.demoApp.dto.WorkSchedulePage import WorkSchedulePage

"""
类名：CreateAccountSever
描述：创建新账号功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
"""
class CheckDepartWorkSchedulePageSever:

    """
    功能阐述:创建新账号功能Sever层主入口
    @:date 2023/4/19
    @:author 常舜志
    """
    def CheckDepartWorkSchedulePage(self,workSchedule):
        try:

            departId = workSchedule.getDepartId()
            staff = workSchedule.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departId in staff.getDepartCode()):
                if(staff.getStaffAutority() >= 2):
                    raise ValueError("您没有操作权限！若您是管理员，请联系信息科系统管理员！")
                checkDepartWorkSchedulePageDao = CheckDepartWorkSchedulePageDao()
                checkDepartWorkSchedulePage = checkDepartWorkSchedulePageDao.CheckDepartWorkSchedulePage(workSchedule)
                checkDepartWorkSchedulePage.setStaff(staff)
                if(checkDepartWorkSchedulePage.__class__ == WorkSchedulePage):
                    departWorkSchedulePageVO = DepartWorkSchedulePageVO()
                    departWorkSchedulePageVO.setVOfromDTO(checkDepartWorkSchedulePage)
                    return departWorkSchedulePageVO
                else:
                    return checkDepartWorkSchedulePage
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e