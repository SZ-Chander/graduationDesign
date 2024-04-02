from backPacket.demoApp.dto import Execute
from flask import current_app
from sqlalchemy import text
"""
类名：CheckExecuteDao
描述：查询执行单功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/31
备注：
"""
class CheckExecuteDao:
    def __init__(self):
        self.executeMessTable = "View_Execute"
        self.db = current_app.config['db']

    """
    功能阐述: 查询执行单功能Dao层主入口
    @:date 2023/3/31
    @:author 常舜志
    """
    def checkExecuteDao(self,departExecute):
        # 读取科室执行单列表
        sqlStr = "select * from {} where departId=:departId and creatTime between :startTime and :endTime".format(self.executeMessTable)
        retData = list(self.db.engine.execute(text(sqlStr), dict(departId=departExecute.getDepartId(),startTime=departExecute.getStartTime(),endTime=departExecute.getEndTime())))
        executeList = []

        for executeMess in retData:
            execute = Execute.Execute()
            execute.setExecute(
                patientId=executeMess[0],patientName=executeMess[1],visitId=executeMess[2],departId=executeMess[3],
                departName=executeMess[4],executeId=executeMess[5],executeSubId=executeMess[6],executeItem=executeMess[7],
                executeSubItem=executeMess[8],staffId=executeMess[9],staffName=executeMess[10],executeLabel=executeMess[11],
                creatTime=executeMess[12],executeTime=executeMess[13],executeKey=executeMess[14],typeCode=executeMess[15],
                typeName=executeMess[16],typeLabel=executeMess[17],completeKey=executeMess[18],completeDate=executeMess[19],
                bedNo=executeMess[20],creatStaff=executeMess[21]
            )
            executeList.append(execute)
        departExecute.setExecuteList(executeList)
        return departExecute