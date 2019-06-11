import oseti

file_name = 'test'
with open('./document/' + file_name + '.txt', mode='r', encoding="utf-8") as text_file:
    analyzer = oseti.Analyzer()
    print(analyzer.analyze(text_file.read()))
