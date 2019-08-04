import wordnet
from wakati_document import wakati


part = '名詞'

word_list = []

with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
    text = wakati(text_file.read(), part)[1]
    word_list.append(text)

print(text)
wn = wordnet.SimilarWord()
wn.similar_word(text)
