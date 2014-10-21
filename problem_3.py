import os

# Setting Variables
str1="systems"
str2="science"
systems_count, science_count, total_count=[0,0,0]


# Opening File
for filename in os.listdir('.'):
    with open('GIS_is_the_best.txt') as f:
        file_contents = f.read().lower()

# Counting words
for word in file_contents.split(' '):
    if word in str1:
        systems_count += 1
    if word in str2:
        science_count += 1    
    total_count += 1

print "Total Words = ", total_count
print "Systems = ", systems_count
print "Science = ", science_count

# Replacing 'science' with 'systems'
'''Checked new science count against old science count and was different
Repeated the for statement above and resulted in same count below. Changed
the elif to an if, and this corrected the count.'''

'''new_science_count=0'''

for word in file_contents.split(' '):
    if word in str2:
        str2.replace("science", "systems",)
        '''new_science_count +=1'''
        systems_count += 1

'''print "New Science Count = ", new_science_count'''
print "New Systems Count =", systems_count

'''So re-running the simple systems_count again was the easiest way to yield
the proper 'systems' count.'''



