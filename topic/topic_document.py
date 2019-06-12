import gensim
from gensim import corpora, models, similarities
import pandas
import numpy as np


def topic(words, file_path):
    dictionary = corpora.Dictionary(words)
    dictionary.filter_extremes(no_below=2, no_above=0.01)

    # コーパスを作成
    corpus = [dictionary.doc2bow(text) for text in words]

    # TF_IDF処理を行ったコーパスを作成
    tf_idf = gensim.models.TfidfModel(corpus)
    corpus_tf_idf = tf_idf[corpus]

    # トピックモデルの作成
    lda = gensim.models.LdaModel(corpus=corpus, id2word=dictionary,
                                 num_topics=50, minimum_probability=0.001,
                                 passes=20, update_every=0, chunksize=10000)

    # topic_top = []
    # for topic_word in lda.show_topics(-1, formatted=False):
    #     topic_top.append([dictionary[int(tag[0])] for tag in topic_word[1]])
    #
    # topic_data = pandas.DataFrame(topic_top)
    # topic_data.to_csv(file_path + "topic_word.csv", encoding='utf-8')

    for i in range(50):
        print('topic_{0}: {1}'.format(i, lda.print_topic(i)[0:80] + '...'))


def topic_detail(words):
    dic_list = []
    for i in range(10):
        dictionary = corpora.Dictionary(words)
        dictionary.filter_extremes(no_below=i + 15, no_above=0.01)
        dic_list.append(dictionary)
        print(i)

    corp_list = []
    for i in range(10):
        print(i)
        corpus = [dic_list[i].doc2bow(text) for text in words]
        corp_list.append(corpus)

    perp_list = []
    for j in range(10):
        for i in range(10):
            lda = gensim.models.ldamodel.LdaModel(corpus=corp_list[i], num_topics=j + 215)
            perp_list.append(np.exp2(-lda.log_perplexity(corpus)))
            print(np.exp2(-lda.log_perplexity(corpus)))
            print('i:', i)
            print('j:', j)
