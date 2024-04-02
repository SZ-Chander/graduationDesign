from backPacket.demoApp.dao.InformationSystem.Login import LoginDao
from backPacket.demoApp.dao.BaseDao import AuthDao
from backPacket.demoApp import config
import time
import jwt
from backPacket.demoApp.tools.usefulTools import UsefulTools

"""
类名：ManageLoginSever
描述：管理员系统登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
"""
class ManageLoginSever:

    """
    功能阐述:管理员系统登录功能Sever层主入口
    @:date 2023/4/19
    @:author 常舜志
    """
    def login(self,inputUser):
        """
        :param inputUser: Controller层传入的实体，类型为dto.User
        :return: 返回Controller层的实体，类型为dto.User
        """
        try:
            loginDao = LoginDao.LoginDao()
            userList = loginDao.login(inputUser)
            if (userList[0].getAutority() > 1):
                raise ValueError("您非管理员用户，请勿登录管理员端")
            try:
                user,id = self.checkCount(userList,inputUser)
            except:
                exception = self.checkCount(userList, inputUser)
                return exception

            saveAuth = AuthDao.AuthDao().saveAuth(user.authToken, id)
            if(saveAuth==True):
                return user
            else:
                raise ValueError("auth保存失败！请联系管理员")
        except Exception as e:
            return e

    """
    功能阐述:用于检查返回的用户数量
    @:date 2023/1/13
    @:author 常舜志
    """
    def checkCount(self,inputList,inputUser):
        """
        :param inputList: 传入的用户列表，类型为list<dto.User>
        :param inputUser: 传入的用户实体，类型为dto.User
        :return: function(x) 检查密码后的实体，类型为dto.User
        """
        lenList = len(inputList)
        if(lenList == 1):
            user = inputList
            return self.checkPassword(inputUser,user)
        elif(lenList > 1):
            try:
                raise ValueError("账户情况异常，请联系管理员，错误代码101")
            except Exception as e:
                return e
        else:
            try:
                raise ValueError("登录失败，请注册或检查账号密码是否正确")
            except Exception as e:
                return e

    """
    功能阐述:检查传入的User实体密码是否正确，并在校验后去除密码
    @:date 2023/1/13
    @:author 常舜志
    """
    def checkPassword(self,inputUser,daoUserList):
        """
        :param inputUser: 传入Sever层时的用户实体，类型为dto.User
        :param outputUser: 从Dto层返回的用户实体，类型为dto.User
        :return: outputUser 返回的用户实体，类型为User
        """
        if (Exception in inputUser.__class__.__bases__):
            return inputUser
        else:
            usefulTools = UsefulTools()
            daoUser = daoUserList[0]
            try:
                if (usefulTools.passwordChecker(daoUser.getPassword(), inputUser.getPassword())):
                    daoUser, id = self.makeAuthToken(inputUser)
                    return daoUser, id
                else:
                    raise ValueError("登录失败，请注册或检查账号密码是否正确")
            except Exception as e:
                return e

    """
    功能阐述:生成AuthToken并将id和密码置空
    @:date 2023/1/17
    @:author 常舜志
    """
    def makeAuthToken(self,inputUser):
        """
        :param inputUser: 传入的用户实体，类型为dto.User
        :return: 传出的用户实体，类型为dto.User
        """
        tokenConfig = config.getConfig()["tokenConfig"]
        id = inputUser.id
        password = inputUser.password
        twoDay = 60 * 60 * 24 * 2
        codeDict = {
            'exp': time.time() + twoDay,
            'iat': time.time(),'iss':tokenConfig['iss'],
            'data': {
                'id': id,
                'password': password
            }
        }
        authToken = jwt.encode(codeDict,tokenConfig['key'],algorithm=tokenConfig['algorithm'])
        inputUser.setAuthToken(authToken)
        return inputUser,id