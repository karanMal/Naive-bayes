#!/usr/bin/env python3
"""mapper2.py"""

import sys 
import re

for line in sys.stdin:
    eg_id=line.strip().split('\t')[0];
    
    line=re.sub(r'[^\w\s]','',line); ## removing punctuation and other small chars
    words= (line.strip().split('\t')[2:])[0].split()[2:];
    words[-1]=words[-1][:-2]; ## removing en from last words 
    words=[w.lower() for w in words]
    
    
    
    #print(words);
   
    #print(words);
    for w in words:
        if(len(w)>1):
#            for label in uniq_labels:

            print('%s\t%s\t%s'%(eg_id,w,1));
