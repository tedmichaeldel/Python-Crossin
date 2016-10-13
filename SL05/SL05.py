# -*- coding: utf-8 -*-

fp = open('Mask_list.txt', 'r')
Mask = []
for word in fp.readlines():
    word = word.strip()
    # word = word.decode()
    Mask.append(word)
fp.close()
print Mask


def block_word(a):
    for word_M in Mask:
        # 有可能有中文的存在，转换为unicode来判断长度，再用‘*’来替代
        a = a.replace(word_M, '*' * len(word_M.decode('utf8')))
    return a


To_be_tested = raw_input('要被检验的文字：')
print block_word(To_be_tested)
