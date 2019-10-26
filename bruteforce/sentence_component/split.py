def blank(InputArray):
    NWord = 0
    Wordarray = ['']
    for i in InputArray:
        if("가"<=i<="힣"):
            Wordarray[NWord] = Wordarray[NWord]+i
        elif("A">=i>="z"):
            Wordarray[NWord] = Wordarray[NWord]+i
        elif("9">=i>="0"):
            Wordarray[NWord] = Wordarray[NWord]+i
        else:
            NWord = NWord +1
            Wordarray.append("")
    return Wordarray  

Array = input ("문장 입력")
Wordarray = blank(Array)
print(Wordarray)