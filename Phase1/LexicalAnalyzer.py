from .Reader import TokenReader
from .TokenizedToken import TokenizedToken
from .Token import Token
from files import files_path

import re

def getTokenIndex(tk):
    return tk.getIndex()

class LexicalAnalyzer:
    
    def __init__(self,code):
        self.tokens=TokenReader().getTokens()
        self.code=code
    def regexMatch(self,token):
        tokenized=[]
        pattern=re.compile(token.getRegex())
        match=re.finditer(pattern,self.code)
        for iter in match:
            tk =TokenizedToken("<" + token.getName() + ">",iter.group(),iter.start())
            tokenized.append(tk)
            self.code=self.code[0:iter.start()]+" "*(iter.end()-iter.start())+self.code[iter.end():]
            #print("match : ",iter.group()," , start : ",iter.start(),", end : ",iter.end())
        return tokenized
    def Tokenize(self):
        tokenized=[]
        for token in self.tokens:
            currentTokenized=self.regexMatch(token)
            # print(currentTokenized)
            if len(currentTokenized)!=0:
                tokenized.extend(currentTokenized)
        tokenized.sort(key=getTokenIndex)
        return tokenized
    


def get_value(value):
    value = value.replace("\t", "")
    value = value.replace("\n", "")
    value = value.strip()
    return value

def process(input_file):
    data = []
    with open(input_file, encoding="utf-8") as file:
        data = file.read()
        file.close()
    L=LexicalAnalyzer(data)
    tokens_name = []
    tokens_value = []
    with open(files_path['output'], mode='w+', encoding="utf-8") as o:
        for tk in L.Tokenize():
            name = tk.getTokenName()
            value = get_value(tk.getToken().rstrip())
            output = name + " : " + value
            tokens_name.append(name[1:-1])
            tokens_value.append(value)
            print(output)
            o.write(output+'\n')
        o.close()
    return tokens_name, tokens_value


if __name__ == "__main__":
    process()
