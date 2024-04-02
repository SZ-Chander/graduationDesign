from flask import Blueprint, request
from backPacket.demoApp.dto.WhiteBoardContent import WhiteBoardContent
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever
from backPacket.demoApp.sever.InformationSystem.WhiteBoard import InsertWhiteBoardContentSever
from backPacket.demoApp.controller.baseController import baseController

routeKey = 'insertWhiteBoardContent'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertWhiteBoardContentController
父类：baseController
描述：新建科室留言板功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/23
"""

class insertWhiteBoardContentController(baseController):
    def __init__(self):
        self.basePath = baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:新建科室留言板功能的Controller层实现入口
    @:date 2023/4/23
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def insertWhiteBoardContent(key=1):
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
            departId = dataDict["departId"]
            content = dataDict["content"]
            redMess = dataDict["redMess"]
            # 装载信息进dto
            whiteBoardContent = WhiteBoardContent()
            whiteBoardContent.setDepartId(departId)
            whiteBoardContent.setCreateUserId(userId)
            whiteBoardContent.setContents(content)
            whiteBoardContent.setRedMess(redMess)
            # 信息装载完成，开始调用sever层
            insertWhiteBoardContentSever = InsertWhiteBoardContentSever.InsertWhiteBoardContentSever()
            retMess = insertWhiteBoardContentSever.insertWhiteBoardContentSever(whiteBoardContent)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertWhiteBoardContentController().fullPath #固定部分，不要删除