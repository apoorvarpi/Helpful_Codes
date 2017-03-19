import os,sys
folder = 'C:/Users/Apoorva/Desktop/Stories'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.mp3dest-id=61899', '.mp3')
       output = os.rename(infilename, newname)