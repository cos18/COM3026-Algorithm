import hangul_lib

class Transform:

    word = ''

    def __init__(self, word_list):
        self.word_list = word_list
        self.noun = []               #명사
        self.pronoun = []            #대명사
        self.numnoun = []            #수사
        self.postposition = []       #조사
        self.help_postposition = []  #보조사
        self.preamal=[]              #선어말어미
        self.endword=[]              #종결어미
        self.connection=[]           #연결어미
        self.verv=[]                 #동사
        self.hangul = hangul_lib.Hangul()
        self.classify()
    
    def classify(self):
        for w in self.word_list:
            self.word = w
            isNoun = False
            isVerv = False
            for j in self.hangul.josa:
                jlen = len(j)
                if len(w)>=jlen and w[-jlen:] == j:
                    self.append_nown(jlen)
                    isNoun = True
                    break
            if isNoun:
                continue
            for k in self.hangul.connection:
                klen = len(k)
                if len(w)>=klen and w[-klen:]==k:
                    self.append_verb(klen)
                    isVerv = True
                    break
            if isVerv:
                continue
            for l in self.hangul.connection:
                llen = len(l)
                if len(w)>=llen and w[-llen:]==l:
                    self.append_verb(llen)
                    break

    def append_nown(self, jlen):
        if jlen==1 and (self.word == '창고' or self.word == '사고'):
            self.noun.append(self.word)
            return
        if (self.word[:-jlen] in self.hangul.numeral):
            self.numnoun.append(self.word[:-jlen])
        elif (self.word[:-jlen] in self.hangul.pronoun):
            self.pronoun.append(self.word[:-jlen])
        else:
            self.noun.append(self.word[:-jlen])
        self.postposition.append(self.word[-jlen:])

    def append_verb(self, klen): #선어말이 있으면
        for m in self.hangul.preamal:
            mlen = len(m)
            if self.word>=mlen and self.word[-mlen:] == m:
                self.preamal.append(self.word[-mlen:])
                self.word=self.word[:-mlen]
                break
        self.verv.append(self.word)
            


    def show_word(self):
        print("입력된 단어 : ", self.word_list)
        print(" 명사 : ", self.noun)
        print(" 대명사 :" , self.pronoun)
        print(" 수사 :",self.numnoun)
        print(" 조사 : ", self.postposition)
        print(" 보조사 : ", self.help_postposition)
        print(" 동사 : ", self.verv)
        print(" 선어말어미: ", self.preamal)
        print(" 연결어미: ", self.connection)
        print(" 종결어미: ", self.endword)


'''
Transform("나에")
Transform("나무에")
Transform("하나에")

Transform("나무에게")
Transform("하나한테")
Transform("그곳에서")
Transform("그곳에게서")



show_word()
'''