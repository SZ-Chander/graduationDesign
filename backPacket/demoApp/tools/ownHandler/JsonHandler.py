"""
类名：JsonHandler
描述：用于传出数据的格式化处理
入参：无初始化入参
出参：无初始化出参
作者：常舜志
完成时间：2023/1/13
备注：所有Controller输出都尽量调用本方法，功能可以继续扩展。
"""
# import gc

class JsonHandler:
    def __init__(self):
        self.messJson = {'code':"",'desc':"",'data':None,'errorCode':''}

    """
    功能阐述:格式化输出处理器
    @:date 2023/1/13
    @:author 常舜志
    """
    def returnJson(self,inputData):
        """
        :param inputData: 未格式化处理的Controller层的最终传出数据，类型为 list<dict> 或 dict 或 str 或 list<str>
        :return: self.messJson 格式化处理后的最终数据，类型为 Json格式的Dict
        """
        try:
            if(Exception in inputData.__class__.__bases__):
                self.messJson['desc'] = repr(inputData)
                self.messJson['code'] = "300"
                self.messJson['data'] = None
                self.messJson['errorCode'] = None
            else:
                self.messJson['desc'] = "操作成功"
                self.messJson['code'] = "200"
                self.messJson['errorCode'] = None
                self.messJson['data'] = {inputData.__class__.__name__:inputData}
        except Exception as e:
            self.messJson['desc'] = repr(e)
            self.messJson['code'] = "300"
            self.messJson['data'] = None
            self.messJson['errorCode'] = None
            print("exc")
        finally:
            return self.messJson