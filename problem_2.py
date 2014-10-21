import os

#Setting Variables
systems="systems"
science="science"
systems_count, science_count, total_count=[0,0,0]

#Define Dictionary
wordcount={}

#Opening File
for filename in os.listdir('.'):
    with open('GIS_is_the_best.txt') as f:
        file_contents = f.read().lower()

#Counting words
for word in file_contents.split(' '):
    if word in systems:
        systems_count += 1
    if word in science:
        science_count += 1
    total_count += 1

print "Total Words = ", total_count
print "Systems = ", systems_count
print "Science = ", science_count


