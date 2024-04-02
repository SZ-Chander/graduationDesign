from backPacket.demoApp.dto.manageSystem import StaffFile
from flask import current_app
from sqlalchemy import text
"""
类名：StaffFileDao
描述：护理记录Dao实现
入参：无初始化入参
出参：无初始化出参
作者：马梓洋 
完成时间：2023/4/21
备注：
"""
class StaffFileDao:
    def __init__(self):
        self.staffFileTable = "View_Staff_File"
        self.db = current_app.config['db']

    """
    功能阐述: 护理记录Dao层主入口
    @:date 2023/3/30
    @:author 马梓洋
    """
    def staffFileDao(self,depart):

        sqlStr = "select * from {} where departId=:departId".format(self.staffFileTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=depart.getDepartId())))

        recordList = []
        for staffFile in retData:
            file = StaffFile.StaffFile()
            # userId,name,userDepartCode,departName,autority,sex,birthDate,IDnumber,
            # address,professional,education,employDate,politics
            file.setStaffFile(
                userId=staffFile[0],name=staffFile[1],userDepartCode=staffFile[2],departName=staffFile[3],autority=staffFile[4],
                sex=staffFile[5],birthDate=staffFile[6],IDnumber=staffFile[7],address=staffFile[8],professional=staffFile[9],
                education=staffFile[10],employDate=staffFile[11],politics=staffFile[12]
            )
            recordList.append(file)
        depart.setStaffList(recordList)
        return depart