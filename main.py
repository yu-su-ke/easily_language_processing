from word_cloud.wakati_document import wakati
from word_cloud.wordcloud_document import create_cloud
from pn.main_oseti import pn_oseti
from related_word.wordnet import SimilarWord

part = '名詞'   # 品詞の指定
file_name = 'doc1'

with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    text = text_file.read()

wakati_text = wakati(text, part)[1]
pn_sum, pn_average = pn_oseti(text)

# ワードクラウド
create_cloud(wakati_text)

# 関連語
wn = SimilarWord()
for word in wakati_text:
    wn.similar_word(word)

# pn値
print('平均 : ' + str(pn_average) + '合計 : ' + str(pn_sum))
