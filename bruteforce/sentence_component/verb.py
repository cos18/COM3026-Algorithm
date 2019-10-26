# ERROR 발생한다고 함

word_list = []
stem = []           #어간
final_ending = []   #어말어미
tp_ending = []       #선어말어미


def Transform(word):

    #전역 변수 선언
    global word_list
    global stem
    global final_ending
    global tp_ending

    word_len = len(word)

    def classify():
    
        #어말어미 1글자
         if (word[word_len-1] == '다' or word[word_len-1] == '자' or \
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
              check_tp(word[:word_len-3)
        
    #선어말어미
    def check_tp(a):
        a_len = len(a)
        if (a[a_len-1] == '시' or a[a_len-1] == '았' or a[a_len-1] == '었' or \
            a[a_len-1] == '더' or a[a_len-1] == '는' or a[a_len-1] == '겠' or ):
            tp_ending.append(a[a_len])
            stem.append(a[:a_len-1]
        elif (a[a_len-2:] == '으시'):
            

    word_list.append(word)
    classify()

def show_word():
    print(" 입력된 단어 : ", word_list)
    print(" 어간 : ", stem)
    print(" 어말어미 : ", final_ending)
    print(" 선어말어미 : ", tp_ending)

Transform("먹이다")


show_word()