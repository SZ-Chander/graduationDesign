from backPacket.demoApp.dao.BaseDao import AuthDao
from backPacket.demoApp.tools.usefulTools import UsefulTools
import jwt
from backPacket.demoApp.config import getConfig


"""
类名：AuthSever
描述：用于读取Auth功能的Sever层
入参：无初始入参
出参：无初始出参
作者：常舜志
完成时间：2023/1/19
备注：本类封装Auth校验功能Sever层
"""

class AuthSever:
    """
    功能阐述: 校验Auth-token
    @:date 2023/1/19
    @:author 常舜志
    """
    def checkAuth(self,authToken):
        """
        :param authToken: 未解析的auth-token，类型为String
        :return: 校验结果，类型为Boolean
        """
        tokenConfig = getConfig()['tokenConfig']
        try:
            passData = jwt.decode(authToken, tokenConfig['key'], issuer=tokenConfig['iss'],
                                  algorithms=tokenConfig['algorithms'])
            data = passData['data']
            id = data['id']
            password = data['password']
            daoPassword = AuthDao.AuthDao().checkAuth(data)
            usefulTools = UsefulTools()
            try:
                usefulTools.passwordChecker(daoPassword,password)
            except:
                raise ValueError("Auth验证失败，请重新登录")
            if((len(daoPassword) != 1) and (type(daoPassword) is not str)):
                raise ValueError("Auth验证失败，请重新登录")
            return id,True
        except:
            # print(id)
            return "000",False

    def checkAuthPassword(self,authToken):
        """
        :param password: 传入的密码，类型为String
        :param authToken: 未解析的auth-token，类型为String
        :return: 校验结果，类型为Boolean
        """
        tokenConfig = getConfig()['tokenConfig']
        try:
            passData = jwt.decode(authToken, tokenConfig['key'], issuer=tokenConfig['iss'],
                                  algorithms=tokenConfig['algorithms'])
            data = passData['data']
            tokenPassword = data['password']
            return True,tokenPassword
        except:
            return False,0