from backPacket.demoApp.dao.BaseDao import CheckStaffMessDao
from backPacket.demoApp.dao.InformationSystem.VitalTask import VitalTaskDao

"""
类名：VitalTaskSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
"""
class VitalTaskSever:

    """
    功能阐述:登录功能Sever层主入口
    @:date 2023/1/13
    @:author 常舜志
    """
    def checkStaffMess(self,inoutStaff):
        try:
            checkStaffMessDao = CheckStaffMessDao.CheckStaffMessDao()
            staff = checkStaffMessDao.checkStaffMess(inoutStaff)
            staff.checkAdmin()
            return staff
        except Exception as e:
            return e
    def vitalTaskSever(self,depart):
        try:
            staff = depart.getStaff()
            departCode = depart.getDepartId()
            if(departCode == None):
                depart.setDepartId(staff.getDepartCode()[0])
            if(depart.getDepartId() in staff.getDepartCode()):
                vitalTaskDao = VitalTaskDao.VitalTaskDao()
                vitalTask = vitalTaskDao.vitalTaskDao(depart)
                self.setDepartName(vitalTask)
                return vitalTask
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def setDepartName(self,depart):
        departMessList = depart.getStaff().getDepart()
        departId = depart.getDepartId()
        for departMess in departMessList:
            if(departId == departMess[0]):
                depart.setDepartName(departMess[1])
                break