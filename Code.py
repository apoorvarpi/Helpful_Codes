import os,sys
folder = '<file name>'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('<from format>', '<to format>')
       output = os.rename(infilename, newname)