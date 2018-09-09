
# coding: utf-8

# In[1]:


import numpy as np

import time

import re
from collections import Counter


# In[2]:


train_start_time=time.time();
train_path='/scratch/ds222-2017/assignment-1/DBPedia.full/full_train.txt';
test_path='/scratch/ds222-2017/assignment-1/DBPedia.full/full_test.txt';
devel_path='/scratch/ds222-2017/assignment-1/DBPedia.full/full_devel.txt';

# # Train Data
# 

# In[3]:


def data_read(path):    
    file = open(path);
    file=file.readlines();

    train_data=[];
    labels=[];

    for line in file:
        
        
        total_labels=line.strip().split('\t')[0];
        
        line=re.sub(r'[^\w\s]','',line); ## removing punctuation and other small chars
        
        train_data.append( (line.strip().split('\t')[1:])[0].split()[2:] );
        
        labels.append(total_labels.split(','));
    
    for i in range(len(train_data)): ## lower chars
        train_data[i]=[word.lower() for word in train_data[i]];
        train_data[i][-1]=train_data[i][-1][:-2]; ## removing en in data
        labels[i][-1]=labels[i][-1][:-1]; ## removing spaces 
        
        
    return train_data,labels;


def label_to_key(labels,dict_):
    for i in range(len(labels)):
        for j in range(len(labels[i])):
            labels[i][j]=dict_[labels[i][j]]
    return labels;





def test_accuracy(data,labels,w_dict,w_count,p_y):
    y_pred=np.zeros((len(data),50));
    
    for i in range(len(data)):
        for word in data[i]:
            if word in w_dict: ## For Unknowns to vocabulary
        #y_pred[i]+= np.log( np.array(w_dict[word])/w_count );
                for j in range(y_pred.shape[1]):
                    y_pred[i][j]+=np.log(w_dict[word][j]/w_count[j]);
        for j in range(y_pred.shape[1]):
            y_pred[i][j]+=np.log(prob_y[j]);
    
            
    

    y_pred=np.argmax(y_pred,axis=1)
    
    #print(len(y_pred),len(labels))
    acc=0;
    for i in range(len(labels)):
        if y_pred[i] in labels[i]:
            acc+=1;
    return(acc/len(y_pred));


# In[4]:



train_data,train_labels=data_read(train_path);
#train_labels


# In[5]:


## dictionary for labels
label_to_index = [word for line in train_labels for word in line]
label_to_index = list(set(label_to_index));
label_to_index={i:j for i,j in zip(label_to_index,range(len(label_to_index))) }


train_labels=label_to_key(train_labels,label_to_index);


# In[6]:


train_labels

prob_y=[l for labels in train_labels for l in labels]

total_c=len(prob_y)

prob_y=Counter(prob_y);


for key in prob_y:
    prob_y[key]/=total_c;
    
prob_y


# In[7]:


dev_data,dev_labels=data_read(devel_path);
dev_labels=label_to_key(dev_labels,label_to_index);


# In[8]:


K=[0.015,0.016]; ## smoothening Factor

dev_acc=[];

for k in K:

    words_dict={}

#     k=1
    for i in range(len(train_data)):
        line=train_data[i];
        for word in line:
            if word not in words_dict:
                words_dict[word]=[k]*50; ## list_of no of classes;

            for l in train_labels[i]:
                words_dict[word][l]+=1;



    words_count=np.zeros((50,));
    for key in words_dict:
        words_count+=list(words_dict[key])




    #print('Train accuracy is %lf'%test_accuracy(train_data,train_labels,words_dict,words_count,prob_y));
    #train_end_time=time.time();

    dev_acc.append(test_accuracy(dev_data,dev_labels,words_dict,words_count,prob_y))

    #print(k,dev_acc[-1]) ## only for validation 


# In[9]:


train_end_time=time.time()


# In[13]:



test_start_time=time.time();

test_data,test_labels=data_read(test_path);
test_labels=label_to_key(test_labels,label_to_index);


# In[15]:


k=0.015 ## best k with validation data

words_dict={}

for i in range(len(train_data)):
    line=train_data[i];
    for word in line:
        if word not in words_dict:
            words_dict[word]=[k]*50; ## list_of no of classes;

        for l in train_labels[i]:
            words_dict[word][l]+=1;



words_count=np.zeros((50,));
for key in words_dict:
    words_count+=list(words_dict[key])


# In[16]:


print('Test accuracy is %lf'%test_accuracy(test_data,test_labels,words_dict,words_count,prob_y));
test_end_time=time.time();


# In[17]:


print('train_time is %lf'%(train_end_time-train_start_time))
print('test_time is %lf'%(test_end_time-test_start_time))

