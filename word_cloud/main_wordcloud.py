from wakati_document import wakati
from wordcloud_document import create_cloud

part = ''

with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
    text, test = wakati(text_file.read(), part)

word_list = " ".join(test)
print(word_list)
create_cloud(word_list)
