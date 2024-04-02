class ChangePasswordC2S:
    def __init__(self):
        self.oldPassword = None
        self.userId = None
        self.newPassword = None
        self.newPasswordAgain = None
        self.authToken  = None
    def setAuthToken(self,authToken):
        self.authToken = authToken
    def setOldPassword(self,oldPassword):
        self.oldPassword = oldPassword
    def setNewPassword(self,newPassword):
        self.newPassword = newPassword
    def setNewPasswordAgain(self,newPasswordAgain):
        self.newPasswordAgain = newPasswordAgain
    def setUserId(self,userId):
        self.userId = userId
    def getOldPassword(self):
        return self.oldPassword
    def getNewPassword(self):
        return self.newPassword
    def getNewPasswordAgain(self):
        return self.newPasswordAgain
    def getUserId(self):
        return self.userId
    def getAuthToken(self):
        return self.authToken