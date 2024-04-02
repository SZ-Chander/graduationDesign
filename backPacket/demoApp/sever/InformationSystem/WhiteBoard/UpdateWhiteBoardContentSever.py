from backPacket.demoApp.TO.UpdateContentS2D import UpdateContentTOS2D
from backPacket.demoApp.dao.InformationSystem.WhiteBoard.UpdateWhiteBoardContentDao import UpdateWhiteBoardContentDao

"""
类名：UpdateWhiteBoardContentSever
描述：更新白板留言Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/24
"""
class UpdateWhiteBoardContentSever:

    """
    功能阐述:更新白板留言Sever层实现类主入口
    @:date 2023/4/24
    @:author 常舜志
    """
    def updateWhiteBoardContentSever(self,updateContentTO):
        try:
            whiteBoardContent = updateContentTO.getWhiteBoardContent()
            contentId = whiteBoardContent.getContentId()
            contentUserId = contentId.split("T")[0].replace("U","")
            if(contentUserId != whiteBoardContent.getEditUserId()):
                raise ValueError("您只能修改自己的留言\n若您是管理员，请使用管理系统修改他人留言")
            modeKey = updateContentTO.getUpdateModeKey()
            valueDict = {"contentId":contentId}
            # modeKey=1,代表标红更新，仅读取redMess
            if(modeKey == 1):
                redMess = whiteBoardContent.getRedMess()
                updateContentTOS2D = self.keyUpdate("redMess",redMess,valueDict)

            # modeKey=2,代表删除(隐藏)更新，仅读取visibleKey
            elif(modeKey == 2):
                visibleKey = whiteBoardContent.getVisibleKey()
                updateContentTOS2D = self.keyUpdate("visibleKey", visibleKey, valueDict)
            # modeKey=3,代表内容更新，读取除以上三个内容外的所有字段
            elif(modeKey == 3):
                content = whiteBoardContent.getContent()
                editId = whiteBoardContent.getEditUserId()
                updateContentTOS2D = self.contentUpdate(content,editId,valueDict)
            # 非法请求
            else:
                raise ValueError("非法请求，请联系管理员\n错误代码U001")
            updateWhiteBoardContentDao = UpdateWhiteBoardContentDao()
            retData = updateWhiteBoardContentDao.updateWhiteBoardContentDao(updateContentTOS2D)

            if(Exception in retData.__class__.__bases__):
                raise ValueError("修改失败，请联系管理员")
            elif(retData == 1):
                return "修改成功！"
            else:
                raise ValueError("修改失败，请检查数据")

        except Exception as e:
            return e

    def keyUpdate(self,funtionName,value,valueDict):
        updateContentTOS2D = UpdateContentTOS2D()
        sqlStr = "set {}=:{}".format(funtionName,funtionName)
        valueDict[funtionName] = value
        updateContentTOS2D.setSqlStr(sqlStr)
        updateContentTOS2D.setValueDict(valueDict)
        updateContentTOS2D.setDaoFuntionKey(1)
        return updateContentTOS2D

    def contentUpdate(self,content,editId,valueDict):
        updateContentTOS2D = UpdateContentTOS2D()
        updateContentTOS2D.setDaoFuntionKey(2)
        sqlStr = ":contentId,:in_newContent,:in_editId"
        valueDict['in_newContent'] = content
        valueDict['in_editId'] = editId
        updateContentTOS2D.setSqlStr(sqlStr)
        updateContentTOS2D.setValueDict(valueDict)
        return updateContentTOS2D