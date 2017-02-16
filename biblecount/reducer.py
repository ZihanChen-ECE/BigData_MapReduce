#!/usr/bin/env python
import sys
current_word, current_count, word=None,1,None

for line in sys.stdin:
    try: 
        line = line.rstrip()
        word, count = line.split("\t", 1)
        count = int(count)
    except: continue
    
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print "%s\t%u" % (current_word, current_count)
        current_count, current_word = count, word
        
if current_word == word:
    print "%s\t%u" % (current_word, current_count)
