from backPacket.demoApp.dao.manageSystem.StaffFile import UpdateStaffFileDao
from backPacket.demoApp.TO.manageSystem import UpdateStaffFileS2D

"""
类名：UpdateStaffFileSever
描述：更新护士档案功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class UpdateStaffFileSever:

    """
    功能阐述:更新护理记录功能Sever层主入口
    @:date 2023/4/19
    @:author 马梓洋
    """
    def updateStaffFileSever(self,departStaffFile):
        try:
            departId = departStaffFile.getDepartId()
            staff = departStaffFile.getStaff()
            key = self.checkKey(departStaffFile)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departStaffFile.getDepartId() in staff.getDepartCode()):
                updateStaffFileDao = UpdateStaffFileDao.UpdateStaffFileDao()
                rowCount = updateStaffFileDao.updateStaffFileDao(key)
                rowCount2=updateStaffFileDao.updateSysUserDao(key)
                if(rowCount == 1 and rowCount2==1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departStaffFile):
        updateStaffFileS2D = UpdateStaffFileS2D.UpdateStaffFileS2D()
        file = departStaffFile.getNursingList()

        # userId,name,userDepartCode,departName,autority,sex,birthDate,IDnumber,
        # address,professional,education,employDate,politics
        updateStaffFileS2D.setUpdateStaffFile(
            name=file.getname(), sex=file.getsex(),birthDate=file.getbirthDate(),IDnumber=file.getIDnumber(),
            address=file.getaddress(),professional=file.getprofessional(),education=file.geteducation(),employDate=file.getemployDate(),
            politics=file.getpolitics()
        )

        updateStaffFileS2D.setStaffFileBaseValues(
            file.getuserId())

        return updateStaffFileS2D