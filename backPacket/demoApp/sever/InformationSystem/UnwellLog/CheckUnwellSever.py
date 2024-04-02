from backPacket.demoApp.dao.InformationSystem.UnwellLog.CheckUnwellDao import CheckUnwellDao
from backPacket.demoApp.VO.UnwellVO import UnwellVo

"""
类名：CheckUnwellSever
描述：登录功能Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/3/24
"""
class CheckUnwellSever:

    """
    功能阐述:执行单查询功能Sever层主入口
    @:date 2023/3/31
    @:author 常舜志
    """
    def checkUnwellSever(self,unwellLogPage):
        try:
            departId = unwellLogPage.getDepartId()
            staff = unwellLogPage.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(unwellLogPage.getDepartId() in staff.getDepartCode()):
                checkUnwellDao = CheckUnwellDao()
                unwellLogPage = checkUnwellDao.checkUnwellDao(unwellLogPage)

                dtoList = unwellLogPage.getUnwellLogList()
                unwellLogPage.setUnwellLogList(list(map(self.dto2VO,dtoList)))
                return unwellLogPage
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

    def dto2VO(self,dto):
        vo = UnwellVo()
        vo.setUnwellVofromDto(dto)
        vo.transKey()
        return vo
