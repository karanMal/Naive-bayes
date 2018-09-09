#!/usr/bin/env python3
"""reducer2.py"""

import sys 
import re
import math

uniq_labels=['Major_League_Baseball_pitchers',
 'American_television_actresses',
 'American_film_actresses',
 'American_male_film_actors',
 'Harvard_University_alumni',
 'American_comedy_films',
 'Association_football_defenders',
 'Articles_containing_video_clips',
 'American_people_of_Irish_descent',
 'Arctiidae',
 'American_military_personnel_of_World_War_II',
 'Italian_footballers',
 'Fellows_of_the_Royal_Society',
 'Association_football_midfielders',
 'English-language_journals',
 'English-language_albums',
 'French_films',
 'Russian_footballers',
 'American_drama_films',
 'Indian_films',
 'English-language_films',
 'Australian_rules_footballers_from_Victoria_(Australia)',
 'Columbia_University_alumni',
 'Association_football_forwards',
 'British_films',
 'German_footballers',
 'Windows_games',
 'Brazilian_footballers',
 'Rivers_of_Romania',
 'American_male_television_actors',
 'American_films',
 'Black-and-white_films',
 'The_Football_League_players',
 'Insects_of_Europe',
 'Villages_in_the_Czech_Republic',
 'American_film_directors',
 'Villages_in_Turkey',
 'English_cricketers',
 'Yale_University_alumni',
 'Deaths_from_myocardial_infarction',
 'Association_football_goalkeepers',
 'Scottish_footballers',
 'English-language_television_programming',
 'English_footballers',
 'Asteroids_named_for_people',
 'Main_Belt_asteroids',
 'Serie_A_players',
 'Italian_films',
 'Hindi-language_films',
 'Guggenheim_Fellows'];




dict_hash={}; ## from training output
f = open("test_dict", 'r')

lines = f.readlines();
for line in lines:
    line=line.strip();
    temp=line.split('\t');
    key,value=temp[0],int(temp[1])
    dict_hash[key]=value; ## training dictionary 

k=0.015; ## smoothening factor 


vocab_size=dict_hash['!word_count'];

prev_eg_id='';
prev_word='';
prev_count=0;

for line in sys.stdin:
    
    line=line.strip();
    
    
    temp = line.split('\t');
    
    eg_id=temp[0];word=temp[1];count=int(temp[2]);
    
    
    
    #print(label_word,label)
    
    if(len(prev_eg_id)==0): ### for first key count 
        prev_eg_id=eg_id;
        prev_word=word;
        prev_count=count;
        
    
    elif(prev_word==word):
        prev_count+=count;
    
    
    else:
        
        for label in uniq_labels:
            
            label_word=label+'^'+prev_word;
            
            if(label_word in dict_hash):
                a=( (dict_hash[label_word]+k)/ (dict_hash[label+'%%%']+(k*vocab_size) ) )
            else:
                a=( (0+k)/ (dict_hash[label+'%%%']+(k*vocab_size)) );
                
            score=math.log(a);

            score=score*prev_count;
            
            new_k=prev_eg_id+'^'+label+'^'+prev_word;
            
            print('%s\t%s'%(new_k,round(score,2)));
        
        prev_eg_id=eg_id;
        prev_word=word;
        prev_count=count;

            
            
            
