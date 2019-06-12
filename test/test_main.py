import MeCab
m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '''
中澤先生、教授へのご就任、誠におめでとうございます。先生のこれまでの研究の成果が認められ、私もとても嬉しく、心より感激しています。今後とも変わらぬご指導・ご鞭撻をいただきますよう何卒宜しくお願い申し上げます。また、くれぐれもご無理などなさらないようご自愛くださいませ。'''
print(m.parse(text))
