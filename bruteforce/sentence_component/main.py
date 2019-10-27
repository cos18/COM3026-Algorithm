import categorize

sentence = input ("문장 입력 ->")
word_list = sentence.split()
sort_list = categorize.Transform(word_list)
sort_list.show_word()