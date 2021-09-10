# StructSony
Python script to backup Sony Image files from the default Memory Card storage format to convenient backup format

## Brief summary

```Sony has an annoying storage structure for the pictures and videos taken in their Mirrorless and DSLRs. The filenames are non-intuitive and they allow you to back up properly only using their software.```

This project helps to extract pictures and videos from Sony's memory card format and paste them, in a clean structured format in a location of your choice.
Following is an example call to make to call this script:

```bash
python main.py "/Volumes/Untitled/" "/Volumes/MEDIA_NM/Photos/Image Archive/A6400"
```
As seen from above, there are two parameters to the script to be passed via Command Line.

The first parameter is the location of the Memory Card that has been used by your Sony Camera.
The above example looks for the Sony file storage structure in the "/Volumes/Untitled" directory.

The second parameter is the desired location of backup. In my case, I have set it to an External Hard Drive.
The format for backup is currently kept as - "Backup_dd.mm.YYYY" where the date will be the date of running the script.

PS - 
This script was developed purely for convenience reasons.
Posting it in Git incase anybody else finds it usefull too. Please feel free to propose any updates to this.

It is still under development. I am not responsible for any data loss/ corruption as a result of execution of this script.
