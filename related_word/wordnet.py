import sqlite3
import pandas as pd
import re


class SimilarWord:
    def __init__(self):
        self.connection = sqlite3.connect("./related_word/wnjpn.db")  # データベース

    # 確認用　普段は使わない
    def confirm_database(self):
        # 含まれるテーブルの要素の確認
        confirm_table = self.connection.execute("select name from sqlite_master where type='table'")
        for row in confirm_table:
            print(row)

        # データの確認
        confirm_data = self.connection.execute("select* from word limit 20")
        for row in confirm_data:
            print(row)

    def search_similar_word(self, word):
        # 問い合わせた単語がWordnetに存在するかを確認する
        query = self.connection.execute("select wordid from word where lemma='%s'" % word)
        word_id = 99999999  # temp
        for row in query:
            word_id = row[0]
        if word_id == 99999999:
            print('「%s」は、Wordnetに存在しない単語です。' % word)
            # 存在しない場合は処理打ち切り
            return
        else:
            print('「%s」の類義語を出力します。' % word)

        # 存在する場合は単語を含む概念を検索する
        query_concept = self.connection.execute("select synset from sense where wordid='%s'" % word_id)
        concept_sets = []
        for row in query_concept:
            concept_sets.append(row[0])

        # 概念に含まれる単語を検索する
        number_concept = 1
        for concept_set in concept_sets:
            # 概念検索
            search_concept = self.connection.execute("select name from synset where synset='%s'" % concept_set)
            for row1 in search_concept:
                print('%sつめの概念 : %s' % (number_concept, row1[0]))
            # 意味検索
            search_meaning = self.connection.execute("select def from synset_def where (synset='%s' and lang='jpn')" % concept_set)
            number_meaning = 1
            for row2 in search_meaning:
                print("意味%s : %s" % (number_meaning, row2[0]))
                number_meaning += 1
            # 類義語検索
            search_word = self.connection.execute("select wordid from sense where (synset='%s' and wordid!=%s)" % (concept_set, word_id))
            number_word = 1
            for row3 in search_word:
                target_word_id = row3[0]
                search_word_detail = self.connection.execute("select lemma from word where wordid=%s AND lang='jpn'" % target_word_id)
                for row3_1 in search_word_detail:
                    # 類義語から英語を弾いた上で上位5件のものを保存
                    if number_word <= 5:
                        print("類義語%s : %s" % (number_word, row3_1[0]))
                        self.save_csv(word, row3_1[0])
                        number_word += 1

            print('\n')
            number_concept += 1

    def similar_word(self, data):
        for word in data:
            # シングルクォーテーションを全角に(エラー回避)
            re.sub("'", "’", word)
            self.search_similar_word(word)

    def save_csv(self, word, value):
        df = pd.DataFrame([[word, value]])
        # CSV ファイルとして出力
        df.to_csv("related_word/result/result.csv", mode='a', header=False, index=False)


if __name__ == '__main__':
    sw = SimilarWord()
    # csvファイル読み込み
    data = pd.read_csv('./data/test.csv', names=['item_id', 'meta', 'attr_value'])
    # sw.confirm_database()
    sw.search_similar_word('アクアリウム')
