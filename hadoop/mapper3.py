#!/usr/bin/env python3
"""mapper3.py"""

import sys 
import re

for line in sys.stdin:
    
    line=line.strip();
    
    temp=line.split('\t');
    
    
    key,value=temp[0],float(temp[1]);
    
    
    temp=key.split('^');
    
    
    key_1=temp[0]+'^'+temp[1];
    
    
    key_2=temp[2];
    
    
    print('%s\t%s\t%s'%(key_1,key_2,value));
