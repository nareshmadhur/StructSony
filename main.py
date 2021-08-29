import os
import shutil
from tqdm import tqdm
import glob
import datetime

newfiles=[]
todaystring=datetime.datetime.today().strftime('%d%b%Y')

sdcard_loc = '/Volumes/Untitled/DCIM/100MSDCF'
backup_loc = '/Volumes/MEDIA_NM/Photos/Image Archive/A6400'

print('Finding new files that have not been backed up...')

for i in tqdm(os.listdir(sdcard_loc)):
    if i[0] != '.' and len(glob.glob(os.path.join(backup_loc,'**/')+i, recursive=True)) == 0:
        newfiles.append(os.path.join(sdcard_loc,i))

print(f'Find completed. Found {len(newfiles)} new photos.')
if len(newfiles)>0:
    newfolder = 'Backup_'+todaystring

    print(f'Creating folder Backup_{newfolder}')

    backup_loc_newfolder = os.path.join(backup_loc,newfolder)
    os.mkdir(backup_loc_newfolder)

    print(f'Folder created. Copying new contents into {backup_loc_newfolder}')

    for newfile in tqdm(newfiles):
        shutil.copy(newfile, os.path.join(backup_loc_newfolder, newfile.split('/')[-1]))

    print(f'Copy complete. All photos from {sdcard_loc} have been backed up into {backup_loc}')
else:
    print('Chill. All files have been backed up. Proceeding to cleaning')
# REMOVE ANY HIDDEN FILES FROM BACKUP TO MAINTAIN CLEANLINESS
print('Cleaning up any hidden files to save storage space...')

hiddenfiles = glob.glob(os.path.join(backup_loc,'**/')+'.*',recursive=True)
for i in hiddenfiles:
    print(f'Removing hidden file {i}...',end='')
    os.remove(i)
    print('Done')

print('Cleanup complete. Exiting now...')


