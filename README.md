# lpfm-podcast-mgmt
Podcast management scripts for Low Power FM radio stations on Windows.

These scripts are for getting podcasts through RSS and through Dropbox. They grab the items from the specified url/dropbox folder and move them into Incoming and Newest folders for the podcast. Incoming currently needs to be manually cleaned up by moving older episodes to Archive. Newest will only ever have the latest episode so that a program like StationPlayList can easily determine which file we want played.

## Setup
### Install Python 3
These scripts have been tested with python 3.11.4. The python-3.11.4-amd64.exe installer will automatically add the correct items to PATH.
  C:\Users\Admin\AppData\Local\Programs\Python\Python311\Scripts\
  C:\Users\Admin\AppData\Local\Programs\Python\Python311\

### Fill out Templates
Currently you have to fill out the templates manually for each show you have, but I'm working on a script that will autofill them based on a spreadsheet. 

### Set up Task Scheduler
Run Task Scheudler as admin. Enable All Tasks History. Create FeedProcessing folder under Task Scheduler Library. Create a new task for each show. Make sure this script runs at least ten minutes before you need the show to air.

1. General
    1. Set the name
    2. Leave user account as admin account
    3. Select Run whether user is logged on or not
    4. Check Do not store password
    5. Check Run with highest privileges
    6. Configure for Windows 10
    7. Keep Hidden unchecked
2. Triggers: New
    1. Begin: On a schedule
    2. Fill out daily/weekly as indicated by schedule
    3. All unchecked except
    4. Check Enabled
3. Actions: New
    1. Action: Start a program
    2. Select script
    3. Leave arguments and start in blank
4. Conditions
    1. Leave checked
        1. Start the task only if the computer is on AC power 
        2. Stop if the computer switches to battery power
    2. Leave unchecked
        1. Idle options
        2. Wake the computer to run this task 
        3. Start only if the following network connection is available
5. Settings
    1. Leave checked
        1. Allow task to be run on demand
        2. Stop the task if it runs longer than
        3. If the running task does not end when requested, force it to stop
    2. Leave unchecked
        1. Run task as soon as possible after a scheduled start is missed
        2. If the task fails, restart every
        3. If the task is not scheduled to run again, delete it after
    3. If the task is already running, then the following rule applies: Do not start a new instance
