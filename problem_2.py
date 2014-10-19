import os
from collections import Counter

path = r'F:/UWTacoma/GIS_501_AU_2014/lab_3/'
dirs = os.listdir( path )


wordcount={}

systems_count, science_count, total_count =[0,0,0]

for filename in os.listdir('.'):
    with open('GIS_is_the_best.txt') as f:
        file_contents = f.read().lower()

for word in file_contents.split(' '):
    if word in wordcount:
        count = wordcount[word]
        total_count += 1
        print total_count
   
print total_count


