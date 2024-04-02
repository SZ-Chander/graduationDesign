from backPacket.demoApp.dao.InformationSystem.ChangePassword.ChangePasswordDao import ChangePasswordDao
from backPacket.demoApp.dto.User import User
from backPacket.demoApp.sever.BaseSever.AuthSever import AuthSever
from backPacket.demoApp.tools.usefulTools import UsefulTools

"""
类名：CheckExecuteSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
"""
class ChangePasswordSever:

    """
    功能阐述:更改密码功能Sever层主入口
    @:date 2023/4/22
    @:author 常舜志
    """
    def changePasswordSever(self,changePasswordC2S):
        usefulTools = UsefulTools()
        try:
            oldPassword = changePasswordC2S.getOldPassword()
            newPassword = changePasswordC2S.getNewPassword()
            newPasswordAgain = changePasswordC2S.getNewPasswordAgain()
            authToken = changePasswordC2S.getAuthToken()
            # 判断更改密码的业务逻辑：旧密码输入正确，同时两次新密码必须一致且新旧密码不能一致
            passwordKey,tokenPassword = AuthSever().checkAuthPassword(authToken)
            if(passwordKey == False):
                raise ValueError("用户令牌读取失败！请重新登录或联系系统管理员！")
            if(tokenPassword != oldPassword):
                raise ValueError("旧密码有误！请重新输入！")
            if(newPassword != newPasswordAgain):
                raise ValueError("新密码确认有误！请重新输入！")
            if(newPassword == oldPassword):
                raise ValueError("新旧密码不能一致！")
            # 没有业务问题，开始装载新密码用户实体
            user = User()
            user.setId(changePasswordC2S.getUserId())
            user.setPassword(usefulTools.passWordHasher(newPassword))
            # 新实体构造完成，调用dao层
            changePasswordDao = ChangePasswordDao()
            userCount = changePasswordDao.changePasswordDao(user)
            if (Exception in userCount.__class__.__bases__):
                return userCount
            else:
                if(userCount == 1):
                    return "密码更改成功！请重新登录！"
                else:
                    raise ValueError("密码更改失败，代码E1001\n请联系系统管理员")

        except Exception as e:
            raise e