#!/usr/bin/env python3
"""mapper1.py"""

import sys 
import re

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



print('%s\t%s'%('!total',1));
print('%s\t%s'%('!word_count',1));

for labels in uniq_labels:
    print('%s\t%s'%(labels+'%%',1));
    print('%s\t%s'%(labels+'%%%',1));

for line in sys.stdin:
    y=line.strip().split('\t')[0];
    y=y.split(',');
    y[-1]=y[-1][:-1]; ## removing spaces from labels

    #print(y);

    line=re.sub(r'[^\w\s]','',line); ## removing punctuation and other small chars
    words= (line.strip().split('\t')[1:])[0].split()[2:];
    words[-1]=words[-1][:-2]; ## removing en from last words 
    words=[w.lower() for w in words]

    for w in words:
        #for label in uniq_labels:
        key=w;

        print('%s\t%s'%(key,1)); #word for every label
