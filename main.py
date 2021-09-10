import os
import shutil
from tqdm import tqdm
import glob
import datetime
import sys

def isProceed():
    proceed = input()
    if proceed in ['y', 'Y']:
        print('Proceeding with default path.')
    else:
        print('Terminating script.')
        exit()

def find_newfiles():
    newfiles = []

    print('\n-------------\nFinding new files that have not been backed up...\n-------------\n')

    for i in tqdm(os.listdir(sdcard_loc)):
        if i[0] != '.' and len(glob.glob(os.path.join(backup_loc, '**/') + i, recursive=True)) == 0:
            newfiles.append(os.path.join(sdcard_loc, i))

    print(f'Find completed. Found {len(newfiles)} new photos.')
    return newfiles


def make_backup(newfiles):
    if len(newfiles) > 0:
        newfolder = 'Backup_' + todaystring

        print(f'\n-------------\nCreating folder Backup_{newfolder}\n-------------\n')

        backup_loc_newfolder = os.path.join(backup_loc, newfolder)
        os.mkdir(backup_loc_newfolder)

        print(f'Folder created. Copying new contents into {backup_loc_newfolder}')

        for newfile in tqdm(newfiles):
            shutil.copy(newfile, os.path.join(backup_loc_newfolder, newfile.split('/')[-1]))

        print(f'Copy complete. All photos from {sdcard_loc} have been backed up into {backup_loc}')
    else:
        print('Chill. All files have been backed up. Proceeding to cleaning')


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
    global sdcard_loc, backup_loc

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

    sdcard_loc = '/Volumes/Untitled/DCIM/100MSDCF'
    backup_loc = '/Volumes/MEDIA_NM/Photos/Image Archive/A6400'

    if len(sys.argv) == 3:
        arg1 = str(sys.argv[1])
        arg2 = str(sys.argv[2])
        validate(arg1, arg2)
    else:
        print(f'Parameters not used. Using default arguments - {sdcard_loc} for SDCard and {backup_loc} for Backup\
Location.\nContinue?')
        isProceed()


    newfiles = find_newfiles()
    make_backup(newfiles)
    cleanup()
