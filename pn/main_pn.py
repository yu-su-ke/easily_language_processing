from pn_document import pn_tweets

file_name = 'test'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    average, pn_sum = pn_tweets(text_file.read())
    print('平均 : ' + average + '合計 : ' + pn_sum)
