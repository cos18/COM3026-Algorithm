word_list = []
noun = []               #명사
pronoun = []            #대명사
numnoun = []            #수사
postposition = []       #조사
help_postposition = []  #보조사

def Transform(word):

    #전역 변수 선언
    global word_list
    global noun
    global pronoun
    global numnoun
    global postposition
    global help_postposition

    word_len = len(word)
    
    def classify():

        #부사격 조사 1글자 짜리
        if (word[word_len-1] == '에' or word[word_len-1] == '로' or \
            word[word_len-1] == '께' or word[word_len-1] == '와' or \
            word[word_len-1] == '과' or word[word_len-1] == '고'):
            check_expection_one()


        #부사격 조사 2글자 짜리
        elif (word[word_len-2:] == '에서' or word[word_len-2:] == '에게' or \
              word[word_len-2:] == '한테' or word[word_len-2:] == '으로' or \
              word[word_len-2:] == '더러' or word[word_len-2:] == '보고' or \
              word[word_len-2:] == '로서' or word[word_len-2:] == '처럼' or \
              word[word_len-2:] == '처럼' or word[word_len-2:] == '만큼' or \
              word[word_len-2:] == '같이' or word[word_len-2:] == '보다' or \
              word[word_len-2:] == '라고'):
            append_two()

        #부사격 조사 3글자 짜리
        elif ( word[word_len-3:] == '에게서' or word[word_len-3:] == '에게로'\
               or word[word_len-3:] == '한테로' or word[word_len-3:] == '으로서'\
               or word[word_len-3:] == '으로써'):
            append_three()

    # 조사 한글자일때 예외
    def check_expection_one():
        if word == '창고' or word == '사고':
            noun.append(word)
        else :
            append_one()

    #조사 한글자일때
    def append_one():
        num = check_pronoun_numnoun(word[:word_len-1])
        if (num == 1):
            pronoun.append(word[:word_len-1])
        elif (num == 2):
            numnoun.append(word[:word_len-1])
        else:
            noun.append(word[:word_len-1])
        postposition.append(word[word_len-1:])

    #조사 두글자일때
    def append_two():
        num = check_pronoun_numnoun(word[:word_len-2])
        if (num == 1):
            pronoun.append(word[:word_len-2])
        elif (num == 2):
            numnoun.append(word[:word_len-2])
        else:
            noun.append(word[:word_len-2])
        postposition.append(word[word_len-2:])
        
    #조사 세글자일때
    def append_three():
        num = check_pronoun_numnoun(word[:word_len-3])
        if (num == 1):
            pronoun.append(word[:word_len-3])
        elif (num == 2):
            numnoun.append(word[:word_len-3])
        else:
            noun.append(word[:word_len-3])
        postposition.append(word[word_len-3:])


    
    def check_pronoun_numnoun(a):
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


            
    word_list.append(word)
    classify()



def show_word():
    print("입력된 단어 : ", word_list)
    print(" 명사 : ", noun)
    print(" 대명사 :" , pronoun)
    print(" 수사 :",numnoun)
    print(" 조사 : ", postposition)
    print(" 보조사 : ", help_postposition)


Transform("나에")
Transform("나무에")
Transform("하나에")

Transform("나무에게")
Transform("하나한테")
Transform("그곳에서")
Transform("그곳에게서")



show_word()