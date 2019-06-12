import oseti

file_name = 'test'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    analyzer = oseti.Analyzer()
    tmp = analyzer.analyze(text_file.read())
    print(tmp)
    print(sum(tmp) / len(tmp))
