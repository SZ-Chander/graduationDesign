from datetime import datetime
from backPacket.demoApp.dao.manageSystem.DepartWorkSchedule.InsertWorkScheduleDao import InsertWorkScheduleDao
"""
类名：InsertWorkScheduleSever
描述：创建新账号功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
"""
class InsertWorkScheduleSever:

    """
    功能阐述:新建排班信息Sever层主入口
    @:date 2023/4/27
    @:author 常舜志
    """
    def insertWorkSchedule(self,workSchedule):
        try:
            staff = workSchedule.getStaff()
            workStaffDepartId = workSchedule.getWorkStaffDepart()
            if(workStaffDepartId in staff.getDepartCode()):
                if(staff.getStaffAutority() > 1):
                    raise ValueError("您无权进行该操作！")
                startTime = datetime.strptime(workSchedule.getStartTime(), '%Y-%m-%d %H:%M:%S')
                endTime = datetime.strptime(workSchedule.getEndTime(), '%Y-%m-%d %H:%M:%S')
                if(endTime <= startTime):
                    raise ValueError("排班起始日期不能晚于或等于结束日期！")

                insertWorkScheduleDao = InsertWorkScheduleDao()
                retData = insertWorkScheduleDao.insertWorkSchedule(workSchedule)
                if(retData == 1):
                    return "排班信息新建成功！"
                elif(retData == -114):
                    raise ValueError("排班信息上传失败，请检查数据是否有误")
                elif(retData == -1):
                    raise ValueError("排班信息上传失败，请联系管理员")
                else:
                    raise ValueError("系统错误，请联系管理员\nCode：1145")
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e