"""
类名：User
描述：用户实体dto
入参：无初始化入参，通过Setter方法进行设置
出参：无初始化出参，通过get方法进行字典化输出
作者：常舜志
完成时间：2023/1/13
备注：实体类修改后务必进行全流程调试！
"""
class User:
    def __init__(self):
        self.password = None
        self.id = None
        self.autority = None
        self.authToken = None
    def setUserFromDict(self,inputDict):
        # self.userName = inputDict["userName"]
        self.password = inputDict["password"]
        self.id = inputDict["id"]
        # self.autority = inputDict["autority"]
    def getUser(self):
        return dict(userName=self.userName,password=self.password,
                    id=self.id,autority=self.autority)
    def setUser(self,userName,password,id,autority):
        self.userName = userName
        self.password = password
        self.id = id
        self.autority = autority

    def setAuthToken(self,inputKey):
        self.authToken = inputKey
        self.id = None
        self.password = None
    def setPassword(self,password):
        self.password = password
    def setId(self,id):
        self.id = id
    def getAutority(self):
        return self.autority
    def getPassword(self):
        return self.password
    def getId(self):
        return self.id