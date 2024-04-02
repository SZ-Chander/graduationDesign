from backPacket.demoApp.dao.manageSystem.StaffFile import StaffFileDao

"""
类名：StaffFileSever
描述：护士信息一览Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/21
"""
class StaffFileSever:


    def staffFileSever(self,depart):
        try:
            staff = depart.getStaff()
            departCode = depart.getDepartId()
            if(departCode == None):
                raise ValueError("departId不能为空")
            if(depart.getDepartId() in staff.getDepartCode()):
                staffFileDao = StaffFileDao.StaffFileDao()
                staffFile = staffFileDao.staffFileDao(depart)
                self.setDepartName(staffFile)
                return staffFile
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

