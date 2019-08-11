from topic_document import topic
from topic_document import topic_detail
from wakati_document import wakati
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.mydb
collection = 'afpbbcom_tweets'
query = db[collection].find().limit(10000)

part = '名詞'

file_path = './csv/'
word_list = []

# with open('./document/test.txt', mode='r', encoding='utf-8') as text_file:
#     # print(text_file.read())
#     wakati_list = wakati(text_file.read(), part)[1]

for tweet in query:
    text = str(wakati(tweet['text'], part)[0])
    word_list.append(wakati(tweet['text'], part)[1])

topic(word_list, file_path)
# topic_detail(word_list)
