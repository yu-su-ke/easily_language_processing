from pn_document import pn_tweets

file_name = 'test'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    print(pn_tweets(text_file.read()))
