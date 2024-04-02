from backPacket.demoApp.dao.InformationSystem.Execute import CheckExecuteDao
from ....tools.usefulTools import UsefulTools

"""
类名：CheckExecuteSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
"""
class CheckExecuteSever:

    """
    功能阐述:执行单查询功能Sever层主入口
    @:date 2023/3/31
    @:author 常舜志
    """
    def checkExecuteSever(self,departExecute):
        try:
            departId = departExecute.getDepartId()
            staff = departExecute.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departExecute.getDepartId() in staff.getDepartCode()):
                checkExecuteDao = CheckExecuteDao.CheckExecuteDao()
                departExecute = checkExecuteDao.checkExecuteDao(departExecute)
                self.setDepartName(departExecute)
                return departExecute
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