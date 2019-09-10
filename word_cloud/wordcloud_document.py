import matplotlib.pyplot as plt
from wordcloud import WordCloud
import platform

# from wakati_document import wakati


def create_cloud(word_list):
    pf = platform.system()
    if pf == 'Windows':
        font_path = r"C:\WINDOWS\Fonts\UDDIGIKYOKASHON-R.TTC"
    elif pf == 'Darwin':
        font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W4.ttc"
    elif pf == 'Linux':
        print('None')
    # ストップワードの設定
    stop_words = [u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して',
                  u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した', u'思う', u'ます',
                  u'それ', u'ここ', u'ちゃん', u'くん', u'って', u'て', u'に', u'を', u'は', u'の', u'が', u'と', u'た', u'し', u'で',
                  u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'から', u'けど',
                  'https', 't', '.', '/', '://', 'co', '@', '_', 'http',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                  '()', '！']
    # print(word_list)
    word_cloud = WordCloud(background_color="black", font_path=font_path, width=3500, height=2000, max_words=500,
                           stopwords=set(stop_words)).generate(word_list)

    plt.figure(figsize=(20, 12))
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()


if __name__ in '__main__':
    part = ''

    with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
        text, test = wakati(text_file.read(), part)

    word_list = " ".join(test)
    print(word_list)
    create_cloud(word_list)
