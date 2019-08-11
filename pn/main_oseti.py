import oseti


def pn_oseti(text):
    analyzer = oseti.Analyzer()
    tmp = analyzer.analyze(text)
    pn_sum = sum(tmp)
    pn_average = sum(tmp) / len(tmp)

    return pn_sum, pn_average


if __name__ == '__main__':
    file_name = 'test'
    with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
        pn_sum, pn_average = pn_oseti(text_file.read())

    print('平均 : ' + str(pn_average) + '合計 : ' + str(pn_sum))
