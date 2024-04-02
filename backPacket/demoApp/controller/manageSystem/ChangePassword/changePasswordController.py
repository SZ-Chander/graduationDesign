from flask import Blueprint, request
from backPacket.demoApp.controller.baseController import baseController
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever
from backPacket.demoApp.sever.InformationSystem.ChangePassword import ChangePasswordSever
from backPacket.demoApp.TO.ChangePasswordC2S import ChangePasswordC2S

routeKey = 'changePassword'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：checkExecuteController
父类：baseController
描述：读取执行单功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/31
"""

class changePasswordController(baseController):
    def __init__(self):
        self.basePath = baseController().basePath #固定部分，不要删除
        self.plusPath = routeKey #固定写法，不要删除
        self.fullPath = super().makeFullPath() #固定写法，不要删除

    """
    功能阐述:更改密码功能的Controller层实现
    @:date 2023/4/22
    @:author 常舜志
    """
    @api_route.route('/', methods=['POST'])
    def changePassword(key=1):
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

            # 用科室代码查询执行单信息
            oldPassword = dataDict["oldPassword"]
            newPassword = dataDict["newPassword"]
            newPasswordAgain = dataDict["newPasswordAgain"]
            # 信息读取完毕，开始设置TO
            changePasswordC2S = ChangePasswordC2S()
            changePasswordC2S.setUserId(userId)
            changePasswordC2S.setOldPassword(oldPassword)
            changePasswordC2S.setNewPassword(newPassword)
            changePasswordC2S.setNewPasswordAgain(newPasswordAgain)
            changePasswordC2S.setAuthToken(token)
            # TO设置完毕，准备进入Sever层
            changePasswordSever = ChangePasswordSever.ChangePasswordSever()
            changeStatus = changePasswordSever.changePasswordSever(changePasswordC2S)
            if (Exception in changeStatus.__class__.__bases__):
                return changeStatus
            else:
                retMess = changeStatus
            # 代码块结束
        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = changePasswordController().fullPath #固定部分，不要删除