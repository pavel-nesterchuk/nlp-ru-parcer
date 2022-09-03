import pandas as pd
import functools
import spacy
from spacy.lang.ru import Russian


def comparator(small_list, big_list):
    small_list_len = len(small_list)
    big_list_len = len(big_list)
    for i in range(0, big_list_len - small_list_len + 1):
        for j in range(small_list_len):
            if small_list[j] != big_list[i+j]:
                break
            if j == small_list_len-1:
                return True
    return False


def comparator_name_dialog(big_list):
    if 'меня' in big_list and 'звать' in big_list:
        return True

def company(big_list):
    for key_word in big_list:
        if key_word == 'компания':
            return True



data = pd.read_csv('test_data.csv', delimiter=',',
                   names=['dlg_id', 'line_n', 'role', 'text'])
nlp = spacy.load("ru_core_news_sm")
pipeline = spacy.load("ru_core_news_sm")
list_dialogov = []
number_mini_dialog = []
for (dlg_id, line_n, role, text) in data[data.role == "manager"].values:
    doc = pipeline(text)
    number_mini_dialog.append(dlg_id)
    mini_dialog = list(map(lambda t: t.lemma_, doc))
    list_dialogov.append(mini_dialog)
    #print(mini_dialog)

privetstvie = [['добрый', 'день'], ['алло', 'здравствовать']]
for dialog, i in zip(list_dialogov, number_mini_dialog):
    if comparator(privetstvie[0], dialog):
        print(i, dialog, 'greeting')
    if comparator(privetstvie[1], dialog):
        print(i, dialog, 'greeting')

for dialog, i in zip(list_dialogov, number_mini_dialog):
    if comparator_name_dialog(dialog):
        print(i, dialog, 'name of manager, name company')

farewell = [['до', 'свидание'], ['всего', 'добрый'], ['вам', 'спасибо'],
            ['всего', 'хороший'], ['до', 'свидания'], ['все', 'хороший']]
for dialog, i in zip(list_dialogov, number_mini_dialog):
    if comparator(farewell[0], dialog):
        print(i, dialog, '_farewell')
    if comparator(farewell[1], dialog):
        print(i, dialog, '_farewell')
    if comparator(farewell[2], dialog):
        print(i, dialog, '_farewell')
    if comparator(farewell[3], dialog):
        print(i, dialog, '_farewell')
    if comparator(farewell[4], dialog):
        print(i, dialog, '_farewell')
    if comparator(farewell[5], dialog):
        print(i, dialog, '_farewell')

