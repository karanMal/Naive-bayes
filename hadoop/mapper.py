#!/usr/bin/env python3
"""mapper.py"""

import sys 
import re

for line in sys.stdin:
    y=line.strip().split('\t')[0];
    y=y.split(',');
    y[-1]=y[-1][:-1]; ## removing spaces from labels
    
    #print(y);
    
    line=re.sub(r'[^\w\s]','',line); ## removing punctuation and other small chars
    words= (line.strip().split('\t')[1:])[0].split()[2:];
    words[-1]=words[-1][:-2]; ## removing en from last words 
    words=[w.lower() for w in words]
    
    
    
    #print(words);
    for label in y:
        # map_out.append(label+'%\t'+'1');
        # map_out.append('!'+'\t'+'1');
        # if(label in y):
        print('%s\t%s'%(label+'%%',1)); ## y=label count 
        print('%s\t%s'%('!total',1)); ## y= any count 
        
        for w in words:
        
            print('%'+w+'\t'+'1'); ## for finding words_count 
            key=label+'^'+w;
            key2=label+'%%%'; ## for y^any    
            print('%s\t%s'%(key,1)); # y=label
            
            print('%s\t%s'%(key2,1));
            #map_out.append(key+'\t'+'1');
                
    
