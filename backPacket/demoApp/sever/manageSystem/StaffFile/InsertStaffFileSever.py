from backPacket.demoApp.dao.manageSystem.StaffFile import InsertStaffFileDao
from backPacket.demoApp.TO.manageSystem import InsertStaffFileS2D

"""
类名：insertStaffFileSever
描述：新增护士档案Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：马梓洋
完成时间：2023/4/23
"""
class InsertStaffFileSever:

    """
    功能阐述:新建护士档案功能Sever层主入口
    @:date 2023/4/23
    @:author 马梓洋
    """
    def insertStaffFileSever(self,departStaffFile):
        try:
            dateStringFormat = "%Y-%m-%d %H:%M:%S"
            dateStringFormat2="%Y%m%d%H%M%S"
            departId = departStaffFile.getDepartId()
            staff = departStaffFile.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(departStaffFile.getDepartId() in staff.getDepartCode()):
                # 设置固定参数
                # userId,sex,birthDate,IDnumber,
                # address,professional,education,employDate,politics
                file = departStaffFile.getNursingList()

                # 装载参数进入TO
                insertStaffFileS2D = InsertStaffFileS2D.InsertStaffFileS2D()
                insertStaffFileS2D.setInsertStaffFileBaseMess(
                    userId=file.getuserId(),sex=file.getsex(),birthDate=file.getbirthDate(),
                    IDnumber=file.getIDnumber(),address=file.getaddress(),professional=file.getprofessional(),
                    education=file.geteducation(),employDate=file.getemployDate(),politics=file.getpolitics()
                )
                # 调用dao层

                insertStaffFileDao = InsertStaffFileDao.InsertStaffFileDao()
                if(insertStaffFileDao.selectUserIdDao(insertStaffFileS2D)==1):
                    raise ValueError("此用户ID已存在档案，无法再次新建!!")
                rowCount = insertStaffFileDao.insertStaffFileDao(insertStaffFileS2D)
                if(rowCount == 1):
                    return True
                else:
                    return rowCount
            else:
                raise ValueError("无权访问该科室/病区")
        except Exception as e:
            return e

    def setDepartName(self,depart):
        departMessList = depart.getStaff().getDepart()
        departId = depart.getDepartId()
        for departMess in departMessList:
            if(departId == departMess[0]):
                depart.setDepartName(departMess[1])
                break