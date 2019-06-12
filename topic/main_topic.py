from topic_document import topic
from wakati_document import wakati

part = '名詞'

file_path = './csv/'
word_list = []

with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
    # print(text_file.read())
    text = wakati(text_file.read(), part)[0]
    word_list.append(wakati(text_file.read(), part)[1])

print(text)
topic(word_list, file_path)
