# -*- coding: utf-8 -*-
# windows 下如果出现编码问题，将 utf-8 改为 cp936

# 读取屏蔽词文件
def load_blocked():
    with open('words.txt') as f:
        global blocked_words  # 使用全局变量记录屏蔽词
        blocked_words = [l.strip() for l in f.readlines() if f]
        # 这里是为了去掉读进来的内容中带有的空格、换行符、空字符等，等同于以下代码
        # blocked_words = []
        # lines = f.readlines()
        # for l in lines:
        #     if l:
        #         l = l.strip()
        #         blocked_words.append(l)


def words_filter(text, charset='utf8', symbol='*'):
    # uni_origin = origin.decode(charset)
    for w in blocked_words:
        # 将每个屏蔽词与待检测文字匹配并替换，默认使用‘*’
        text = text.replace(w, symbol * len(w.decode(charset)))
        # 这里用 w.decode(charset) 的长度，是为了将字符传转为 unicode 再计算长度
        # 否则一个中文字符的长度会是 2 或者 3，这里 charset 默认 utf-8，也可调用时指定
    return text


# 测试效果
if __name__ == '__main__':
    # 读取屏蔽词
    load_blocked()
    while True:
        t = raw_input('输入文字(直接回车退出)：\n')
        if not t:
            break
        print words_filter(t)  # 输出替换结果
