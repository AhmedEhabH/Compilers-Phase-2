class Token:
    def __init__(self,name,tiny,regex):
        self.name=name
        self.tiny=tiny
        self.regex=regex
    def getName(self):
        return self.name
    def getTiny(self):
        return self.tiny
    def getRegex(self):
        return self.regex
    def setName(self,name):
        self.name=name
    def setTiny(self,tiny):
        self.tiny=tiny
    def setRegex(self,regex):
        self.regex=regex
    