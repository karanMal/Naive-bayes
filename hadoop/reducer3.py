#!/usr/bin/env python3
"""reducer3.py"""


import sys 
import re

prev_key='';
prev_count=0;

for line in sys.stdin:
    
    line=line.strip();
    
    
    temp = line.split('\t');
    
    
    key,count=temp[0],float(temp[2]);
    
    
    
    
    #print(key,count)
    
    if(len(prev_key)==0): ### for first key count 
        prev_key=key;
        prev_count=count;
        
    
    elif(prev_key==key):
        prev_count+=count;
    
    
    else:
        print('%s\t%s'%(prev_key,str(prev_count)) );
        prev_key=key;
        prev_count=count;
    
    