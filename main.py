from word_cloud.wakati_document import wakati
from word_cloud.wordcloud_document import create_cloud
from pn.pn_document import pn_tweets

part = ''

with open('./document/doc1.txt', mode='r', encoding='utf-8') as text_file:
    text = wakati(text_file.read(), part)[0]
    average, pn_sum = pn_tweets(text_file.read())

print('平均 : ' + average + '合計 : ' + pn_sum)
print(text)
create_cloud(text)
