import os
import shutil
from tqdm import tqdm
import glob
import datetime
import sys
import filecmp

def isProceed():
    proceed = input()
    if proceed in ['y', 'Y']:
        print('Proceeding with default path.')
    else:
        print('Terminating script.')
        exit()


def find_newphotos():
    newphotos = []
    print('\n-------------\nFinding new photos that have not been backed up...\n-------------\n')

    for i in tqdm(os.listdir(os.path.join(sdcard_loc, sdcard_ploc))):
        same_filenames = glob.glob(os.path.join(backup_loc, '**/') + i, recursive=True)
        if i[0] != '.':
            if not any([filecmp.cmp(os.path.join(sdcard_loc, sdcard_ploc) + '/' + i, j) for j in same_filenames]):
                newphotos.append(os.path.join(os.path.join(sdcard_loc, sdcard_ploc), i))
    print(f'Find completed. Found {str(len(newphotos))} new photos.')
    return newphotos


def find_newvids():
    newvids = []
    print('\n-------------\nFinding new video files that have not been backed up...\n-------------\n')

    for i in tqdm(os.listdir(os.path.join(sdcard_loc, sdcard_vloc))):
        same_filenames = glob.glob(os.path.join(backup_loc, '**/') + i, recursive=True)
        if i[0] != '.' and (i[-4:]).upper() != '.XML':
            if not any([filecmp.cmp(os.path.join(sdcard_loc, sdcard_vloc)+'/'+i,j) for j in same_filenames]):
                newvids.append(os.path.join(os.path.join(sdcard_loc, sdcard_vloc), i))
    print(f'Find completed. Found {len(newvids)} new videos.')
    return newvids


def make_backup(newphotos, newvids):
    if len(newphotos) > 0 or len(newvids)>0:
        newfolder = 'Backup_' + todaystring

        print(f'\n-------------\nCreating folder Backup_{newfolder}\n-------------\n')

        backup_loc_newfolder = os.path.join(backup_loc, newfolder)
        if os.path.exists(backup_loc_newfolder):
            print('Folder Already exists. Dumping pictures in the same folder.')
        else:
            os.mkdir(backup_loc_newfolder)
        print(f'Folder created. Copying new contents into {backup_loc_newfolder}')
    else:
        print('No new photos or videos to backup. Check back later.')
    if len(newphotos)>0:

        print(f'Photos - copying {str(len(newphotos))} photos to Backup drive.')
        for newphoto in tqdm(newphotos):
            shutil.copy(newphoto, os.path.join(backup_loc_newfolder, newphoto.split('/')[-1]))
        print(f'Copy complete. All photos from {sdcard_loc}\nhave been backed up into {backup_loc}')
    else:
        print('No photos to backup. Everything has been backed up already.')

    if len(newvids)>0:
        print(f'Videos - copying {str(len(newvids))} videos to Backup drive.')
        for newvid in tqdm(newvids):
            shutil.copy(newvid, os.path.join(backup_loc_newfolder, newvid.split('/')[-1]))
        print(f'Copy complete. All videos from {sdcard_loc}\nhave been backed up into {backup_loc}')
    else:
        print('No videos to backup. Everything has been backed up already.')

# REMOVE ANY HIDDEN FILES FROM BACKUP TO MAINTAIN CLEANLINESS
def cleanup():
    print('\n-------------\nCleaning up any hidden files to save storage space...\n-------------\n')

    hiddenfiles = glob.glob(os.path.join(backup_loc, '**/') + '.*', recursive=True)
    if len(hiddenfiles) == 0:
        print('All good here. It\'s clean already.')
    for i in hiddenfiles:
        print(f'Removing hidden file {i}...', end='')
        os.remove(i)
        print('Done')

    print('Cleanup complete. Exiting now...')
    print('\n-------------\nRUN COMPLETE\n-------------\n')


def validate(arg1, arg2):
    global sdcard_loc, backup_loc, sdcard_ploc, sdcard_vloc

    if not os.path.exists(arg1):
        print(f'SDCARD Path not valid. Choose default path? \n({sdcard_loc}) [Y/n]:')
        isProceed()
    else:
        sdcard_loc = arg1

    if not os.path.exists(arg2):
        print(f'BACKUP Path not valid. Choose default path? \n({backup_loc}) [Y/n]:')
        isProceed()
    else:
        backup_loc = arg2


if __name__ == '__main__':

    print('\n-------------\nSONY SDCARD BACKUP SCRIPT\n-------------\n')
    todaystring = datetime.datetime.today().strftime('%d%b%Y')

    sdcard_loc = '/Volumes/Untitled/'
    sdcard_ploc = 'DCIM/100MSDCF'
    sdcard_vloc = 'PRIVATE/M4ROOT/CLIP'
    backup_loc = '/Volumes/MEDIA_NM/Photos/Image Archive/A6400'

    if len(sys.argv) == 3:
        arg1 = str(sys.argv[1])
        arg2 = str(sys.argv[2])
        validate(arg1, arg2)
    else:
        print(f'Parameters not used. Using default arguments\nSONY SD CARD: {sdcard_loc}, and\nBACKUP DRIVE: {backup_loc} for Backup\
Location.\nPress Y to continue')
        isProceed()

    newphotos = find_newphotos()
    newvids = find_newvids()
    make_backup(newphotos, newvids)
    cleanup()
