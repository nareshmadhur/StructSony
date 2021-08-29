import os
import shutil
from tqdm import tqdm
import glob
import datetime

newfiles=[]

print('Finding new files that have not been backed up...')

for i in tqdm(os.listdir('/Volumes/Untitled/DCIM/100MSDCF')):
    if len(glob.glob('/Volumes/Media_NM/**/' + 'DSC04183.JPG',recursive=True))!=0:
        newfiles.append(os.path.abspath(i))

print(f'Find completed. Found {len(newfiles)} new photos.')
print(f'Creating folder Backup_{datetime.datetime.today().strftime("%d%b%Y")}')
