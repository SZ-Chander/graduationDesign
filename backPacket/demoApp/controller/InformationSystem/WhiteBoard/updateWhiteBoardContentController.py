from flask import Blueprint, request
from backPacket.demoApp.TO.UpdateContentC2S import UpdateContentTO
from backPacket.demoApp.dto.WhiteBoardContent import WhiteBoardContent
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever
from backPacket.demoApp.sever.InformationSystem.WhiteBoard import UpdateWhiteBoardContentSever
from backPacket.demoApp.controller.baseController import baseController

routeKey = 'updateWhiteBoardContent'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：updateWhiteBoardContentController
父类：baseController
描述：修改/删除科室留言板功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/23
"""

class updateWhiteBoardContentController(baseController):
    def __init__(self):
        self.basePath = baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:修改/删除科室留言板功能的Controller层实现入口
    @:date 2023/4/24
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def updateWhiteBoardContent(key=1):
        """
        :return: jsonHandler(retMess) 经过jsonHandler格式化处理后的执行单信息
        """
        retMess = 0
        try:
            # 以下这一段基本上可以copy到所有json输入的非login的Controller代码中
            dataDict = {}
            for item in request.json:
                dataDict[item] = request.json[item] #将request中的信息读取出来
            token = request.headers.get('AuthToken') #获取请求标头中的auth-token
            userId, authCorrect = AuthSever.AuthSever().checkAuth(token) #校验auth-token是否正确
            if(authCorrect != True):
                raise ValueError("Auth校验失败，请重新登录")
            # 以上是格式逻辑，以下开始功能实现

            # 加载前端信息
            content = dataDict["content"]
            redMess = dataDict["redMess"]
            visibleKey = dataDict['visibleKey']
            updateModeKey = dataDict['updateModeKey']
            contentId = dataDict['contentId']

            # 装载信息进dto
            whiteBoardContent = WhiteBoardContent()
            whiteBoardContent.setEditUserId(userId)
            whiteBoardContent.setContents(content)
            whiteBoardContent.setRedMess(redMess)
            whiteBoardContent.setVisibleKey(visibleKey)
            whiteBoardContent.setContentId(contentId)
            # 将dto装载金to
            updateContentTO = UpdateContentTO()
            updateContentTO.setWhiteBoardContent(whiteBoardContent)
            updateContentTO.setUpdateModeKey(int(updateModeKey))

            # 信息装载完成，开始调用sever层
            updateWhiteBoardContentSever = UpdateWhiteBoardContentSever.UpdateWhiteBoardContentSever()
            retMess = updateWhiteBoardContentSever.updateWhiteBoardContentSever(updateContentTO)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = updateWhiteBoardContentController().fullPath #固定部分，不要删除