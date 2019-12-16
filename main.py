from glob import glob
from tqdm import tqdm

from wakati_document import wakati
from word_cloud.wordcloud_document import create_cloud
from positive_negative.main_oseti import pn_oseti
from related_word.wordnet import SimilarWord
from topic.topic_document import topic

part = '名詞'   # 品詞の指定
file_name = 'kokoro_format'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    text = text_file.read()
wakati_text = wakati(text, part)

# ワードクラウドの作成
print('ワードクラウド作成中・・・')
word_list = " ".join(wakati_text)
create_cloud(word_list)
print('ワードクラウド完成!')

# 関連語の抽出
print('関連語の抽出中・・・')
wn = SimilarWord()
for word in tqdm(wakati_text):
    wn.similar_word(word)
print('関連語の抽出終了！')

# pn値の算出
pn_sum, pn_average = pn_oseti(text)
print('平均 : ' + str(pn_average) + '合計 : ' + str(pn_sum))

# トピックの抽出
# トピック抽出は多くの文書が必要になるので、livedoorコーパスなどを使います
dir_name = './document/livedoor/dokujo-tsushin'
word_list = []
for file_name in glob(dir_name + '/*.txt'):
    with open(file_name, mode='r', encoding="utf-8") as text_topic:
        text = text_topic.read()
        word_list.append(wakati(text, part))
topic(word_list)
