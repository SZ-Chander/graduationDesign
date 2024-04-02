from flask import Blueprint, request
from backPacket.demoApp.dto import Staff, UnwellLog
from backPacket.demoApp.tools.ownHandler import JsonHandler
from backPacket.demoApp.sever.BaseSever import AuthSever, CheckStaffMessSever
from backPacket.demoApp.sever.InformationSystem.UnwellLog import InsertUnwellLogSever
from backPacket.demoApp.controller.baseController import baseController
from backPacket.demoApp.tools.usefulTools import UsefulTools

routeKey = 'insertUnwellLog'
api_route = Blueprint(routeKey, __name__) #固定部分，不要删除

"""
类名：insertUnwellLogController
父类：baseController
描述：新建科室留言板功能的Controller层实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/27
"""

class insertUnwellLogController(baseController):
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
    def insertUnwellLogController(key=1):
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
            # 用userID查表获得工作人员dto
            staff = Staff.Staff()
            staff.setStaffId(userId)
            checkStaffMessSever = CheckStaffMessSever.CheckStaffMessSever()
            staff = checkStaffMessSever.checkStaffMess(staff)
            # staff信息查询完毕，开始查询入参信息
            staffId = dataDict['staffId']
            happenTime = dataDict['happenTime']
            happenTime = UsefulTools().mandarinDate2Format(happenTime,"%Y-%m-%d %H:%M:%S","%Y年%m月%d日 %H:%M:%S")
            storyContent = dataDict['storyContent']
            storyLevel = dataDict['storyLevel']
            departId = dataDict['departId']
            # 前端入参读取完毕，开始装载信息
            unwellLog = UnwellLog.UnwellLog()
            # userId(无需读取)
            unwellLog.setCreateId(userId)
            # staffId(输入)
            unwellLog.setStaffId(staffId)
            # happenTime(输入)
            unwellLog.setHappenTime(happenTime)
            # storyContent(输入)
            unwellLog.setStoryContent(storyContent)
            # storyLevel(输入)
            unwellLog.setStoryLevel(storyLevel)
            # statusCode(读取staff权限)
            unwellLog.setStatusCode(staff)
            # departId（输入）
            unwellLog.setDepartId(departId)
            # 传入sever层
            insertUnwellLogSever = InsertUnwellLogSever.InsertUnwellLogSever()
            retMess = insertUnwellLogSever.insertUnwellLog(unwellLog)

        except Exception as e:
            retMess = e
        finally:
            return JsonHandler.JsonHandler().returnJson(retMess)


fullPath = insertUnwellLogController().fullPath #固定部分，不要删除