from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：InsertExecuteDao
描述：新建执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/5
备注：
"""
class InsertExecuteDao:
    def __init__(self):
        self.createLogProcedure = "CreateNewExecuteLog"
        self.createSubLogProcedure = "CreateNewExecuteSubLog"
        self.db = current_app.config['db']

    """
    功能阐述: 查询执行单功能Dao层主入口
    @:date 2023/4/5
    @:author 常舜志
    """
    def insertExecuteDao(self,execute,modeKey):
        # 读取科室执行单列表
        if(modeKey==0):
            sqlStr,dataDict = self.insertLog(execute)
        elif(modeKey==1):
            sqlStr,dataDict = self.insertSubLog(execute)
        else:
            raise ValueError("系统错误，请联系管理员")
        self.db.session.execute(text(sqlStr), dataDict)
        self.db.session.commit()
        self.db.session.close()
        return 1

    def insertLog(self,execute):
        patientId = execute.getPatientId()
        visitId = execute.getvisitId()
        createStaffId = execute.getStaffId()
        executeItem = execute.getExecuteItem()
        executeSubItem = execute.getExecuteSubItem()
        executeLabel = execute.getExecuteLabel()
        typeCode = execute.getTypeCode()
        createStaff = execute.getCreatStaff()
        sqlStrProcedure = 'CALL {}(:patientId,:visitId,:executeItem,:executeSubItem,:executeLabel,:typeCode,:createStaff,:createStaffId)'.format(self.createLogProcedure)
        dataDict = dict(patientId=patientId,visitId=visitId,createStaffId=createStaffId,executeItem=executeItem,executeSubItem=executeSubItem,executeLabel=executeLabel,typeCode=typeCode,createStaff=createStaff)
        return sqlStrProcedure,dataDict

    def insertSubLog(self,execute):
        patientId = execute.getPatientId()
        visitId = execute.getvisitId()
        executeId = execute.getExecuteId()
        createStaffId = execute.getStaffId()
        executeItem = execute.getExecuteItem()
        executeSubItem = execute.getExecuteSubItem()
        executeLabel = execute.getExecuteLabel()
        typeCode = execute.getTypeCode()
        createStaff = execute.getCreatStaff()
        sqlStrProcedure = 'CALL {}(:patientId,:visitId,:executeId,:executeItem,:executeSubItem,:executeLabel,:typeCode,:createStaff,:createStaffId)'.format(self.createSubLogProcedure)
        dataDict = dict(patientId=patientId,visitId=visitId,executeId=executeId,executeItem=executeItem,executeSubItem=executeSubItem,executeLabel=executeLabel,typeCode=typeCode,createStaff=createStaff,createStaffId=createStaffId)
        return sqlStrProcedure,dataDict
