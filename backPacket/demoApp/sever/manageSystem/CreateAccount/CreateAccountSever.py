from backPacket.demoApp.dao.manageSystem.CreateAccount.CreateAccountDao import CreateAccountDao

"""
类名：CreateAccountSever
描述：创建新账号功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/19
"""
class CreateAccountSever:

    """
    功能阐述:创建新账号功能Sever层主入口
    @:date 2023/4/19
    @:author 常舜志
    """
    def createAccountSever(self,createrStaff,newStaff):
        try:
            departId = newStaff.getDepartCode()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(newStaff.getDepartCode() in createrStaff.getDepartCode()):
                if(newStaff.getStaffAutority() <= createrStaff.getStaffAutority()):
                    raise ValueError("创建人权限不得低于或等于被创建人\n若需要管理员权限，请先注册一般权限后联系信息科修改")
                succeedKey = CreateAccountDao().creatAccountDao(newStaff)
                if(succeedKey==1):
                    retStr = "新用户{} , 工号{} \n创建成功".format(newStaff.getStaffName(),newStaff.getDepartCode())
                else:
                    retStr = "新用户{} , 工号{} \n创建失败\n请检查信息是否正确或是否已创建".format(newStaff.getStaffName(), newStaff.getDepartCode())
                return retStr
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e