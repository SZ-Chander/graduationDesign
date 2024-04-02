from flask import current_app
from sqlalchemy import text
"""
类名：CheckStaffMessDao
描述：检查工作人员权限的Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/29
备注：
"""

class CheckStaffMessDao:
    """
    功能阐述:查询工作人员信息功能Dao层主入口
    @:date 2023/3/24
    @:author 常舜志
    """
    def __init__(self):
        self.staffMessTable = "View_Staff_DepartMess"
        self.departMessTable = "Table_Depart"
        self.db = current_app.config['db']

    def checkStaffMess(self, staff):
        """
        :param staff: 从Sever层传入的用户实体，类型为dto.Staff
        :return: staffList: 返回Sever层的用户实体列表，类型为list<dto.Staff>
        """
        try:
            sqlStr = "select * from {} where staffId=:staffId".format(self.staffMessTable)
            retData = list(self.db.engine.execute(text(sqlStr),dict(staffId=staff.staffId)))

            assert len(retData) == 1
            departCode = retData[0][2]
            departName = retData[0][3]
            departCodeList = []
            departNameList = []
            if(departCode!="000"):#非管理员
                departCodeList = departCode.split("$")
                departNameList = departName.split("$")
            else:
                sqlDepartStr = "select departId,departName from {}".format(self.departMessTable)
                departList = list(self.db.engine.execute(sqlDepartStr))
                for i in departList:
                    departCodeList.append(i[0])
                    departNameList.append(i[1])

            staffId = retData[0][0]
            staffName = retData[0][1]
            staffAutority = int(retData[0][4])
            staff.setStaff(staffId,staffName,departCodeList,departNameList,staffAutority)

            return staff
        except Exception as e:
            return e
