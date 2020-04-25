from .Token import Token
from files import files_path


class TokenReader:
    def __init__(self):
        self.Tokens=[]
        self.Tokens=self.getTokens()
    def getTokens(self):
        Tokens=[]
        tk=open(files_path['tokens'], encoding="utf8")
        tkTiny=open(files_path['tiny'], encoding="utf8")
        regexFile=open(files_path['regex'], encoding="utf8")
        for i in range(0,75):
            token=tk.readline().strip()
            tiny=tkTiny.readline().strip()
            regex=regexFile.readline().strip()
            TOKEN=Token(token,tiny,regex)
            Tokens.append(TOKEN)
        return Tokens

