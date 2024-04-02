from backPacket.demoApp.dto import Execute
from flask import current_app
from backPacket.demoApp.tools.usefulTools import UsefulTools
from sqlalchemy import text
"""
类名：InsertUnwellLogDao
描述：新建不良事件报告信息Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
备注：
"""
class InsertUnwellLogDao:
    def __init__(self):
        self.procedure = "InsertUnwellLog"
        self.db = current_app.config['db']

    """
    功能阐述: 新建不良事件报告信息Dao层主入口
    @:date 2023/4/27
    @:author 常舜志
    """
    def InsertUnwellLog(self,unwellLog):
        try:
            sqlStr = 'CALL {}(:in_createId,:in_staffId,:in_happenTime,:in_storyContent,:in_storyLevel,:in_statusCode,:in_departId)'.format(self.procedure)
            dataDict = dict(in_createId=unwellLog.getCreateId(),in_staffId=unwellLog.getStaffId(),
                            in_happenTime=unwellLog.getHappenTime(),in_storyContent=unwellLog.getStoryContent(),
                            in_storyLevel=unwellLog.getStoryLevel(),in_statusCode=unwellLog.getStatusCode(),in_departId=unwellLog.getDepartId())

            self.db.session.execute(text(sqlStr),dataDict)
            self.db.session.commit()
            self.db.session.close()
            retData = "新建不良事件报告成功！"

        except Exception as e:
            print("Error as {}".format(e))
            retData = "新建不良事件报告失败，请重试!"
        finally:
            return retData