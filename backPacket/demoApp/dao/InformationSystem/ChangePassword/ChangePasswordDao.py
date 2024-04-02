from flask import current_app

"""
类名：ChangePasswordDao
描述：更改密码功能Dao实现
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/22
备注：
"""
class ChangePasswordDao:
    def __init__(self):
        self.procedure = "ChangePassword"
        self.db = current_app.config['db']

    """
    功能阐述: 更改密码功能Dao层主入口
    @:date 2023/4/22
    @:author 常舜志
    """
    def changePasswordDao(self,inputUser):
        # 通过存储过程读取白板信息
        sqlStr = 'CALL {}("{}","{}", @out_UserCount)'.format(self.procedure,inputUser.getId(),inputUser.getPassword())
        self.db.session.execute(sqlStr)
        retData = list(self.db.session.execute('SELECT @out_UserCount'))
        self.db.session.commit()
        self.db.session.close()
        return retData[0][0]