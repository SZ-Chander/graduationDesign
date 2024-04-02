from backPacket.demoApp.dao.InformationSystem.WhiteBoard import CheckWhiteBoardDao
from backPacket.demoApp.dto import WhiteBoard

"""
类名：CheckWhiteBoardSever
描述：获取护理白板信息Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/13
"""
class CheckWhiteBoardSever:

    """
    功能阐述:护理白板信息查询功能Sever层主入口
    @:date 2023/4/12
    @:author 常舜志
    """
    def checkWhiteBoardSever(self,whiteBoardRoutines):
        try:
            departId = whiteBoardRoutines.getDepartId()
            staff = whiteBoardRoutines.getStaff()
            if(departId == None):
                raise ValueError("departId不能为空")
            if(whiteBoardRoutines.getDepartId() in staff.getDepartCode()):
                # 科室校验成功，进dao层
                checkWhiteBoardDao = CheckWhiteBoardDao.CheckWhiteBoardDao()
                whiteBoardRoutines,listContents = checkWhiteBoardDao.checkWhiteBoardDao(whiteBoardRoutines)
                # 读取存储过程成功，将to转为dto
                whiteBoard = WhiteBoard.WhiteBoard()
                whiteBoard = self.whiteBoardTO2Dto(to=whiteBoardRoutines,dto=whiteBoard)
                whiteBoard.setListContent(listContents)
                staffNameList = whiteBoard.getWorkingStaffNameList()
                nameListStr = ",".join(list(set(staffNameList)))
                whiteBoard.setStaffListStr(nameListStr)
                retDataDict =  whiteBoard.getDataDict()

                pieImgDataList = []
                usedBedData = dict(value=retDataDict["usedBedNum"],name="已用床位数")
                pieImgDataList.append(usedBedData)
                unusedBedData = dict(value=(retDataDict["totoalBedNum"]-retDataDict["usedBedNum"]), name="未使用床位数")
                pieImgDataList.append(unusedBedData)
                retDataDict['pieImgDataList']=pieImgDataList

                return retDataDict
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
    def whiteBoardTO2Dto(self,to,dto):
        dto.setStaff(to.getStaff())
        dto.setDepartId(to.getDepartId())
        dto.setOutPatientNum(to.getOutPatientCount())
        dto.setInPatientNum(to.getEnterPatientCount())
        dto.setUsedBedNum(to.getUsingBedCount())
        dto.setTotalBedNumByStr(to.getBedDict(),"$")
        dto.setWorkingStaffNum(to.getWorkingStaffCount())
        dto.setWorkingStaffNameListByStr(to.getWorkingStaffNameStr(),",")
        return dto