from wakati_document import wakati
from word_cloud.wordcloud_document import create_cloud
from positive_negative.main_oseti import pn_oseti
from related_word.wordnet import SimilarWord

part = '名詞'   # 品詞の指定
file_name = 'doc1'

with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    text = text_file.read()
wakati_text = wakati(text, part)

# ワードクラウドの作成
# create_cloud(wakati_text)

# 関連語の抽出
wn = SimilarWord()
for word in wakati_text:
    wn.similar_word(word)

# pn値の算出
pn_sum, pn_average = pn_oseti(text)
print('平均 : ' + str(pn_average) + '合計 : ' + str(pn_sum))
