import oseti

file_name = 'test'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    analyzer = oseti.Analyzer()
    tmp = analyzer.analyze(text_file.read())
    print(tmp)
    print(sum(tmp) / len(tmp))

file_name2 = 'doc1'
with open('./document/' + file_name2 + '.txt', mode='r', encoding='utf-8') as text_file2:
    analyzer = oseti.Analyzer()
    tmp2 = analyzer.analyze(text_file2.read())
    print(tmp2)
