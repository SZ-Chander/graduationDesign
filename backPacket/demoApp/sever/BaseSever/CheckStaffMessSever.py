from backPacket.demoApp.dao.BaseDao import CheckStaffMessDao

"""
类名：CheckStaffMessSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
"""
class CheckStaffMessSever:

    """
    功能阐述:检查工作人员权限Sever层主入口
    @:date 2023/3/24
    @:author 常舜志
    """
    def checkStaffMess(self,inputStaff):
        """
        :param inputStaff: Controller层传入的实体，类型为dto.Staff
        :return: 返回Controller层的实体，类型为dto.Staff
        """
        try:
            checkStaffMessDao = CheckStaffMessDao.CheckStaffMessDao()
            staff = checkStaffMessDao.checkStaffMess(inputStaff)
            staff.checkAdmin()
            staff.getDepart()
            return staff
        except Exception as e:
            return e