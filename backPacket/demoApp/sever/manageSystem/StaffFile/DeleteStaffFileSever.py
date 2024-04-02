from backPacket.demoApp.dao.manageSystem.StaffFile import DeleteStaffFileDao
from backPacket.demoApp.TO.manageSystem import DeleteStaffFileS2D

"""
类名：DeleteStaffFileSever
描述：删除护士档案功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/19
"""
class DeleteStaffFileSever:


    def deleteStaffFileSever(self,departStaffFile):
        try:
            departId = departStaffFile.getDepartId()
            staff = departStaffFile.getStaff()
            key = self.checkKey(departStaffFile)
            if(key==False):
                raise ValueError("参数无效，请检查参数")
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departStaffFile.getDepartId() in staff.getDepartCode()):
                deleteStaffFileDao = DeleteStaffFileDao.DeleteStaffFileDao()
                if(deleteStaffFileDao.selectUserIdDao(key)==0):
                    raise ValueError("此用户ID已存在档案，无法再次新建!!")
                rowCount = deleteStaffFileDao.deleteStaffFileDao(key)
                if(rowCount == 1 ):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def checkKey(self,departStaffFile):
        deleteStaffFileS2D = DeleteStaffFileS2D.DeleteStaffFileS2D()
        file = departStaffFile.getNursingList()
        deleteStaffFileS2D.setDeleteStaffFileBaseValues(file.getuserId())
        return deleteStaffFileS2D