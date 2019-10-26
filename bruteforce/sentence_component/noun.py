class Transform:

    word = ''

    def __init__(self, word_list):
        self.word_list = word_list
        self.noun = []               #명사
        self.pronoun = []            #대명사
        self.numnoun = []            #수사
        self.postposition = []       #조사
        self.help_postposition = []  #보조사
        self.classify()
    
    def classify(self):
        josa_one = ['에', '로', '께', '와', '과', '고']
        josa_two = ['에서', '에게', '한테', '으로', '더러', \
            '보고', '로서', '처럼', '만큼', '같이' '보다', '라고']
        josa_three = ['에게서', '에게로', '한테로', '으로서', '으로써']

        for w in self.word_list:
            self.word = w
            if (len(w)>0 and (self.word[-1] in josa_one)):
                self.check_expection_one()
            elif (len(w)>1 and (self.word[-2:] in josa_two)):
                self.append_two()
            elif (len(w)>2 and (self.word[-3:] in josa_three)):
                self.append_three()

    # 조사 한글자일때 예외
    def check_expection_one(self):
        if self.word == '창고' or self.word == '사고':
            self.noun.append(self.word)
        else :
            self.append_one()

    #조사 한글자일때
    def append_one(self):
        num = self.check_pronoun_numnoun(self.word[:-1])
        print(num)
        if (num == 1):
            self.pronoun.append(self.word[:-1])
        elif (num == 2):
            self.numnoun.append(self.word[:-1])
        else:
            self.noun.append(self.word[:-1])
        self.postposition.append(self.word[-1:])

    #조사 두글자일때
    def append_two(self):
        num = self.check_pronoun_numnoun(self.word[:-2])
        if (num == 1):
            self.pronoun.append(self.word[:-2])
        elif (num == 2):
            self.numnoun.append(self.word[:-2])
        else:
            self.noun.append(self.word[:-2])
        self.postposition.append(self.word[-2:])
        
    #조사 세글자일때
    def append_three(self):
        num = self.check_pronoun_numnoun(self.word[:-3])
        if (num == 1):
            self.pronoun.append(self.word[:-3])
        elif (num == 2):
            self.numnoun.append(self.word[:-3])
        else:
            self.noun.append(self.word[:-3])
        self.postposition.append(self.word[-3:])

    def check_pronoun_numnoun(self, a):
        #대명사
        if (a == "나" or a == "저" or a == "우리" or a == "저희" or a == "너" \
            or a == "자네" or a == "당신" or a == "그대" or a == "너희" \
            or a == "이이" or a == "이애" or a == "이분" or a == "그이" \
            or a == "저이" or a == "그분" or a == "그애" or a == "그" \
            or a == "저분" or a == "저애" or a == "누구" or a == "아무" \
            or a == "저희" or a == "자기" or a == "이것" or a == "여기" \
            or a == "그곳" or a == "거기" or a == "그것" or a == "이곳" \
            or a == "저것" or a == "저기" or a == "저곳" or a == "어디"):
            return 1
        #수사
        elif (a == '하나' or a == '둘' or a == '셋' or a == '넷' or \
            a == '다섯' or a == '여섯' or a == '일곱' or a == '여덟' or \
            a == '아홉' or a == '열' ):
            return 2
        else :
            return

    def show_word(self):
        print("입력된 단어 : ", self.word_list)
        print(" 명사 : ", self.noun)
        print(" 대명사 :" , self.pronoun)
        print(" 수사 :",self.numnoun)
        print(" 조사 : ", self.postposition)
        print(" 보조사 : ", self.help_postposition)


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