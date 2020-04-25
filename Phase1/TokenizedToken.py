class TokenizedToken:
    def __init__(self,tokenName,token,index):
        self.tokenName=tokenName
        self.token=token
        self.index=index
    def getTokenName(self):
        return self.tokenName
    def getToken(self):
        return self.token
    def getIndex(self):
        return self.index
    def setToken(self,token):
        self.token=token
    def setTokenName(self,tokenName):
        self.tokenName=tokenName
    def setIndex(self,index):
        self.index=index
        