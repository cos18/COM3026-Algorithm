def blank(sentence):
    index = 0
    word = ['']
    for i in sentence:
        if("가"<=i<="힣"):
            word[index] = word[index]+i
        elif("A">=i>="z"):
            word[index] = word[index]+i
        elif("9">=i>="0"):
            word[index] = word[index]+i
        else:
            index = index +1
            word.append("")
    return word  

'''
Array = input ("문장 입력 ->")
word = blank(Array)
print(word)
'''