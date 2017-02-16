#!/usr/bin/env python
import jieba
import sys

for line in sys.stdin:
    wlist = jieba.cut(line.strip())
    for word in wlist:
        try:
            print "%s\t1" % (word.encode("utf8"))
        except:
            pass
