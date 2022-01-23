#! python3
# -*- coding: utf-8 -*-

from collections import Counter
import jieba


def get_words(txt):
    jieba.load_userdict("year")
    seg_list = jieba.cut(txt,cut_all = True)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k, v) in c.most_common(100000):

        print('%s%s %d' % ('' * (5 - len(k)), k, v))


if __name__ == '__main__':
    f = open("splited02.txt", encoding='utf-8')
    get_words(f.read())
    f.close()

