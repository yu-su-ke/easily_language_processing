import MeCab
m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '''
テスト
'''
print(m.parse(text))
