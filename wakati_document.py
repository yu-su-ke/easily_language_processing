import MeCab
import re
import platform


def wakati(text, part):
    pf = platform.system()
    if pf == 'Windows':
        mecab = MeCab.Tagger('-Owakati')
    elif pf == 'Darwin':
        mecab = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    elif pf == 'Linux':
        mecab = MeCab.Tagger("-Owakati -d /usr/lib/mecab/dic/mecab-ipadic-neologd/")
    mecab.parse('')
    node = mecab.parseToNode(text)
    output = []

    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            if part == '名詞':
                word_type = node.feature.split(",")[0]
                if word_type in [part]:
                    output.append(node.surface)
            elif part == '固有名詞':
                word_type = node.feature.split(",")[1]
                if word_type in [part]:
                    output.append(node.surface)
                # word_type2 = node.feature.split(",")[2]
                # if word_type in ["人名", "地域"] and node.surface not in stop_words:
                #   output.append(node.surface)
                # elif word_type in ["組織"] and node.surface.isalpha() is False:
                #     output.append(node.surface)
            elif part == '':
                if len(node.surface) > 1:
                    output.append(node.surface)
        node = node.next
        if node is None:
            break

    # print(output)
    return output


def format_text(text):
    text = re.sub(r'[!-~]', "", text)
    return text
