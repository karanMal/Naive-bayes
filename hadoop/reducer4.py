#!/usr/bin/env python3
"""reducer4.py"""

import sys 
import re

prev_key='';
prev_count=0;
prev_label='';
for line in sys.stdin:
    
    line=line.strip();
    
    
    temp = line.split('\t');
    
    if(len(temp)==2):
        key,count=temp[0],float(temp[1]);
        
        
        temp=key.split('^');
        
        key=temp[0];
        
        label=temp[1];
        
        if(len(prev_key)==0): ### for first key count 
            prev_key=key;
            prev_count=count;
            prev_label=label;
        
        elif(prev_key==key):
            if(count>prev_count):
                prev_label=label;
                prev_count=count;
        
        
        else:
            print('%s\t%s'%(prev_key,prev_label) );
            prev_key=key;
            prev_label=label;
            prev_count=count;
        
    