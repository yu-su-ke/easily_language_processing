from topic_document import topic
from wakati_document import wakati

part = '固有名詞'

file_path = './csv/'
word_list = []

with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
    text = str(wakati(text_file, part)[0])
    word_list.append(wakati(text, part)[1])
    topic(text_file, file_path)
