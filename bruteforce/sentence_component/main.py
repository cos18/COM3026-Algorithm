import categorize
import os

choice = ''
while not (choice == '1' or choice == '2'):
    choice = input("입력 형태를 선택하세요 (1-콘솔창에서 직접 입력 / 2-가져올 파일 경로 입력): ")
    if choice == '1':
        sentence = input("문장 입력 ->")
    elif choice == '2':
        directory = input("경로를 입력해주세요 : ")
        if os.path.isfile(directory):
            f = open(os.path.normpath(directory),'r',encoding='UTF8')
            sentence = f.read()
            f.close
        else:
            print("경로가 잘못되었습니다.")
            choice = ''
    else:
        print("잘못 입력하셨습니다. 다시 시도해주세요")

word_list = sentence.split()
sort_list = categorize.Transform(word_list)
sort_list.show_word()