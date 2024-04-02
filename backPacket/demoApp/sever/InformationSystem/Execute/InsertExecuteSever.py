from backPacket.demoApp.dao.InformationSystem.Execute import InsertExecuteDao
import datetime
import backPacket.demoApp.tools.usefulTools as usefulTools
from backPacket.demoApp.TO import InsertExecuteS2D

"""
类名：insertExecuteSever
描述：新建执行单Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/5
"""
class InsertExecuteSever:

    """
    功能阐述:新建执行单功能Sever层主入口
    @:date 2023/4/5
    @:author 常舜志
    """
    def insertExecuteSever(self,departExecute,modeKey):
        try:
            departId = departExecute.getDepartId()
            staff = departExecute.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departExecute.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                execute = departExecute.getExecuteList()
                creatStaff = "{}护士".format(staff.getStaffName())
                execute.setCreatStaff(creatStaff)
                # 调用dao层
                insertExecuteDao = InsertExecuteDao.InsertExecuteDao()
                rowCount = insertExecuteDao.insertExecuteDao(execute,modeKey)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
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

    def getNewExecuteId(self,execute,staff):
        staffId = staff.getStaffId()
        if(execute.getExecuteId() == None):
            timeKey = usefulTools.UsefulTools().dateTime2String(datetime.datetime.now(),"%Y%m%s%h%M%s")
            return "{}N{}".format(staffId,timeKey)
        else:
            return execute.getExecuteId()