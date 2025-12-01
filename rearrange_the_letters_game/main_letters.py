import random

def shuffle_word(word):
    char_list = list(word)
    random.shuffle(char_list)
    return ''.join(char_list)

word = input()
print(shuffle_word(word))