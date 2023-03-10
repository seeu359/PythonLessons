# Функция get_type_of_sentence() различает вопросительные, восклицательные
# и обычные предложения. В зависимости от этого на экран выводится
# определенная
# строка.

def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'

    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type
