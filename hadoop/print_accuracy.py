#!/usr/bin/env python3
"""print_accuracy.py"""



import numpy as np

test_path='/home/kmkaran212/results/full_test_id.txt';
#test_path='/home/karan/verysmall_train_id.txt'
#print(test_path)

file=open(test_path);

file=file.readlines();

# map_out=[];

org_labels={};

for line in file:
    eg_id=line.strip().split('\t')[0];
    y=line.strip().split('\t')[1];
    y=y.split(',');
    y[-1]=y[-1][:-1]; ## removing spaces from labels
    
    org_labels[eg_id]=y;


path='/home/kmkaran212/results/out4.txt';
file=open(path,'r');
file=file.readlines();

pred_labels={};

for line in file:
    eg_id=line.strip().split('\t')[0];
    y=line.strip().split('\t')[1];
    
    pred_labels[eg_id]=y;



sum_=0;

for i in range(0,len(org_labels)):
    if  i!=8 and pred_labels[str(i+1)]  in org_labels[str(i+1)] :
        sum_+=1;
        

print('Test Accuracy is coming to be {0}'.format(sum_/len(org_labels)));
