import MeCab
import pandas as pd
import csv
import platform
import re
from statistics import mean


def pn_tweets(text):
    # pnTableの用意
    pn_df = pd.read_csv('pnTable.txt',
                        sep=':',
                        quoting=csv.QUOTE_NONE,
                        encoding='utf-8',
                        names=('Word', 'Pseudonym', 'POS', 'PN')
                        )
    word_list = list(pn_df['Word'])
    pn_list = list(pn_df['PN'])
    pn_dict = dict(zip(word_list, pn_list))

    pf = platform.system()
    if pf == 'Windows':
        mecab = MeCab.Tagger('')
    elif pf == 'Darwin':
        mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    elif pf == 'Linux':
        mecab = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd/")

    mecab_print = mecab.parse(text)
    lines = mecab_print.split('\n')  # 解析結果を1行（1語）ごとに分けてリストにする
    lines = lines[0:-2]  # 後ろ2行は不要なので削除
    # 形態素解析されたツイートを入れる配列
    dic_list = []
    for word in lines:
        line = re.split('\t|,', word)  # 各行はタブとカンマで区切られてるので
        d = {'Surface': line[0], 'POS1': line[1], 'POS2': line[2], 'BaseForm': line[7]}
        # ソーシャルゲーム[0]	名詞[1],固有名詞[2],一般,*,*,*,ソーシャルゲーム[7],ソーシャルゲーム,ソーシャルゲーム
        dic_list.append(d)

    # dic_listの中身をpnTableと照合した結果を入れる配列
    dic_pn = []
    for word in dic_list:
        base = word['BaseForm']  # 個々の辞書から基本形を取得
        if base in pn_dict:
            pn = float(pn_dict[base])  # 中身の型があれなので
            word['PN'] = pn
            dic_pn.append(word)
            print(word)
        else:
            pn = 'notfound'  # その語がPN Tableになかった場合
            word['PN'] = pn
            dic_pn.append(word)

    pn_list = []
    pn_add = 0
    # 各ツイートのPN値の平均を算出
    for word in dic_pn:
        pn = word['PN']
        if pn != 'notfound':
            pn_list.append(pn)  # notfoundだった場合は追加もしない
            pn_add += pn
    if len(pn_list) > 0:  # 「全部notfound」じゃなければ
        pn_mean = mean(pn_list)
    else:
        pn_mean = 0  # 全部notfoundならゼロにする

    # 確認用
    # print('\n' + str(dic_pn))
    # print(pn_add)

    return str(pn_mean), str(pn_add)


if __name__ == '__main__':
    file_name = 'test'
    with open('./document/' + file_name + '.txt', mode='w', encoding="utf-8") as text_file:
        print('平均 : ' + pn_tweets(text_file.read())[0] + '合計 : ' + pn_tweets(text_file.read())[1])
