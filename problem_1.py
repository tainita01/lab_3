import os, sys

# Opening the folder
abspath = "F:/UWTacoma/GIS_501_AU_2014/lab_3"
folder = abspath + '/text_files'
files = os.listdir(folder)

# Defining the variables
basefile = ""
filename = {}
ext1=['.rtf','.py','.text']

# Renaming with the for loop
for filename in files:
  infilename = os.path.join(folder,filename)
  base_file, ext = os.path.splitext(filename)
  newname = base_file + '.txt'
  output = os.rename(infilename, newname)
