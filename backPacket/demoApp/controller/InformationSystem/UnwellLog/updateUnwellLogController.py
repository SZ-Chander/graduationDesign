from flask import Blueprint, request
from backPacket.demoApp.controller.baseController import baseController
from backPacket.demoApp.dto.UnwellLog import UnwellLog
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever
from backPacket.demoApp.sever.InformationSystem.UnwellLog import UpdateUnwellSever
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'updateUnwellLog'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateUnwellLogController
父类：baseController
描述：读取护理白板信息功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
"""

class updateUnwellLogController(baseController):
    def __init__(self):
        self.basePath = baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:读取护理白板信息功能的Controller层实现
    @:date 2023/4/27
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def checkExecute(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的执行单信息
        """
        retMess = 0
        keyDict = {"一级事件":1,"二级事件":2,"三级事件":3,"四级事件":4,"未审核":0,"护士长审核完成":1,"护理部审核完毕":2}
        try:
            usefulTools = UsefulTools()
            # 以下这一段基本上可以copy到所有json输入的非login的Controller代码中
            dataDict = {}
            for item in request.json:
                dataDict[item] = request.json[item] #将request中的信息读取出来
            token = request.headers.get('AuthToken') #获取请求标头中的auth-token
            userId, authCorrect = AuthSever.AuthSever().checkAuth(token) #校验auth-token是否正确
            if(authCorrect != True):
                raise ValueError("Auth校验失败，请重新登录")
            # 以上是格式逻辑，以下开始功能实现
            logId = dataDict['logId']
            storyContent = dataDict['storyContent']
            storyLevel = dataDict['storyLevel']
            statusCode = dataDict['statusCode']
            # 入参信息读取完毕，开始装载dto
            storyLevel = usefulTools.strDictFilter(storyLevel,keyDict)
            statusCode = usefulTools.strDictFilter(statusCode,keyDict)
            unwellLog = UnwellLog()
            unwellLog.setLogId(logId)
            unwellLog.setStoryContent(storyContent)
            unwellLog.setStaffId(userId)
            unwellLog.setStoryLevel(storyLevel)
            unwellLog.setStatusCode(statusCode)
            # 入参信息装载完毕，开始调用sever层
            updateUnwellSever = UpdateUnwellSever.UpdateUnwellSever()
            retMess = updateUnwellSever.updateUnwellSever(unwellLog)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateUnwellLogController().fullPath #固定部分，不要删除