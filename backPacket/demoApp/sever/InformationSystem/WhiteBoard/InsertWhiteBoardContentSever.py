from backPacket.demoApp.dao.InformationSystem.WhiteBoard.InsertWhiteBoardContentDao import InsertWhiteBoardContentDao

"""
类名：InsertWhiteBoardContentSever
描述：插入白板留言Sever层实现类
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/4/23
"""
class InsertWhiteBoardContentSever:

    """
    功能阐述:执行单查询功能Sever层主入口
    @:date 2023/4/23
    @:author 常舜志
    """
    def insertWhiteBoardContentSever(self,whiteBoardContent):
        try:
            insertWhiteBoardContentDao = InsertWhiteBoardContentDao()
            retData = insertWhiteBoardContentDao.insertWhiteBoardContentDao(whiteBoardContent)
            if(retData == True):
                return "成功新建护理白板信息!"
            else:
                raise ValueError("新建白板信息失败，请重试!")
        except Exception as e:
            return e