word_list = []
noun = []               #명사
pronoun = []            #대명사
postposition = []       #조사
help_postposition = []  #보조사
connection_pronoun = [] #접속조사
stem = []         # 어간
final_ending = [] # 어말어미
tp_ending = []    # 선어말어미

def Transform(word):

    #전역 변수 선언
    global word_list
    global noun
    global pronoun
    global postposition
    global help_postposition
    global connection_pronoun
    global stem
    global final_ending
    global tp_ending

    word_len = len(word)
    
    def classify():

        #부사격 조사 1글자 짜리
        if (word[word_len-1] == '에' or word[word_len-1] == '로' or \
            word[word_len-1] == '께' or word[word_len-1] == '와' or \
            word[word_len-1] == '과' or word[word_len-1] == '고' ):
            check_expection_one()


        #부사격 조사 2글자 짜리
        elif (word[word_len-2:] == '에서' or word[word_len-2:] == '에게' or \
              word[word_len-2:] == '한테' or word[word_len-2:] == '으로' or \
              word[word_len-2:] == '더러' or word[word_len-2:] == '보고' or \
              word[word_len-2:] == '로서' or word[word_len-2:] == '처럼' or \
              word[word_len-2:] == '처럼' or word[word_len-2:] == '만큼' or \
              word[word_len-2:] == '같이' or word[word_len-2:] == '보다' or \
              word[word_len-2:] == '라고'):
            check_expection_two()

        #부사격 조사 3글자 짜리
        elif ( word[word_len-3:] == '에게서' or word[word_len-3:] == '에게로'\
               or word[word_len-3:] == '한테로' or word[word_len-3:] == '으로서'\
               or word[word_len-3:] == '으로써'):
            check_expection_three()

        #을 or 를
        elif (word[word_len-1] == '을' or word[word_len-1] == '를'):
            check_exception_EL_REL()

        elif (word[word_len-1] == '과' or word[word_len-1] == '와' or \
              word[word_len-1] == '나' or word[word_len-1] == '도' or \
              word[word_len-1] == '까지' or word[word_len-1] == '만' or \
              word[word_len-1] == '부터' or word[word_len-1] == '마저'):
            check_exception_WA_GWA()

        ###################### 동사 ####################
            
        #어말어미 1글자
        elif (word[word_len-1] == '다' or word[word_len-1] == '자' or \
              word[word_len-1] == '고' or word[word_len-1] == '며' or \
              word[word_len-1] == '나' or word[word_len-1] == '러' or \
              word[word_len-1] == '면' or word[word_len-1] == '고' or \
              word[word_len-1] == '아' or word[word_len-1] == '어' or \
              word[word_len-1] == '지' or word[word_len-1] == '게' or \
              word[word_len-1] == '고' or word[word_len-1] == '기' or \
              word[word_len-1] == '는' or word[word_len-1] == '은' or \
              word[word_len-1] == '을' or word[word_len-1] == '던' or \
              word[word_len-1] == '게' ):
            final_ending.append(word[word_len-1])
            check_tp(word[:word_len-1])
            
        #어말어미 2글자
        elif (word[word_len-2:] == '구나' or word[word_len-2:] == "느냐" or \
              word[word_len-2:] == '어라' or word[word_len-2:] == '으며' or \
              word[word_len-2:] == '지만' or word[word_len-2:] == '으나' or \
              word[word_len-2:] == '아서' or word[word_len-2:] == '어서' or \
              word[word_len-2:] == '으면' or word[word_len-2:] == '니까' or \
              word[word_len-2:] == '도록' or word[word_len-2:] == '듯이'):
            final_ending.append(word[word_len-2:])
            check_tp(word[:word_len-2])
              
        #어말어미 3글자
        elif (word[word_len-3:] == '으니까'):
            final_ending.append(word[word_len-3:])
            check_tp(word[:word_len-3])

        else: noun.append(word)

    ####################################################


    # 조사 한글자일때 예외
    def check_expection_one():
        if (word == '창고' or word == '사고' or word == '예고' or word == '무고' or \
           word == '사과' or word == '효과' or word == '결과' or word == '통과' or \
           word == '바로' or word == '가로' or word == '세로' or word == '도로'):
            noun.append(word)
        else :
            append_one()

    # 조사 두글자일때 예외
    def check_expection_two():
        #if word == '창고' or word == '사고':
        #    noun.append(word)
        #else :
        #    append_two()
        append_two()   # 예외 못찾아서 임시

    # 조사 세글자일때 예외
    def check_expection_three():
        #if word == '창고' or word == '사고':
        #    noun.append(word)
        #else :
        #    append_three()
        append_three() # 예외 못찾아서 임시

    #조사 한글자일때
    def append_one():
        noun.append(word[:word_len-1])
        help_postposition.append(word[word_len-1:])

    #조사 두글자일때
    def append_two():
        noun.append(word[:word_len-2])
        help_postposition.append(word[word_len-2:])
        
    #조사 세글자일때
    def append_three():
        noun.append(word[:word_len-3])
        help_postposition.append(word[word_len-3:])

    #선어말어미 ( 수정 중 )
    def check_tp(a):
        a_len = len(a)
        if (a[a_len-1] == '시' or a[a_len-1] == '았' or a[a_len-1] == '었' or \
            a[a_len-1] == '더' or a[a_len-1] == '는' or a[a_len-1] == '겠' ):
            tp_ending.append(a[1:a_len])
            stem.append(a[0])
            
        elif (a[a_len-2:] == '으시'):
            tp_ending.append(a[a_len-2:])
            stem.append(a[:a_len-2])

    #을 or 를
    def check_exception_EL_REL():
        if word == '마을' or word == '가을' or word == '리을' or word == '주을' or word == '늦가을':
            noun.append(word)
        else : EL_REL()

    def EL_REL():
        noun.append(word[:word_len-1])
        postposition.append(word[word_len-1:])

    def check_exception_WA_GWA():
        if  (word == '하나' or word == '누나' or word == '그러나' or word == '얼마나' or word =='더구나') :
            noun.append(word)
        else : WA_GWA()

    def WA_GWA():
        noun.append(word[:word_len-1])
        connection_pronoun.append(word[word_len-1:])
           
    word_list.append(word)
    classify()

def show_word():
    print("입력된 단어 : ", word_list)
    print(" 명사 : ", noun)
    print(" 조사 : ", postposition)
    print(" 보조사 : ", help_postposition)
    print(" 어간 : ", stem)
    print(" 어말어미 : ", final_ending)
    print(" 선어말어미 : ", tp_ending)


Transform("가나다라에게")
#Transform("먹이다")
Transform("먹었었어")
Transform("나를")
Transform("하나")


show_word()