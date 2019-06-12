from wakati_document import wakati
from wordcloud_document import create_cloud

part = ''

with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
    text = wakati(text_file.read(), part)[0]

print(text)
create_cloud(text)
