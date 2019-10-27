import split
import categorize

sentence = input ("문장 입력 ->")
word_list = split.blank(sentence)
sort_list = categorize.Transform(word_list)
sort_list.show_word()
