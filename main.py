import os
import shutil
import tqdm
import glob

count=0
for i in os.listdir('/Volumes/Untitled/DCIM/100MSDCF'):
    if len(glob.glob('/Volumes/Media_NM/**/' + 'DSC04183.JPG',recursive=True))!=0:
        count+=1
print(count)