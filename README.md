# EPS - EVE Profile Sync
A simple Python script to sync the settings of multible EVE Online client settings

## Plot
Since I spent a lot of time copying and synchronizing the settings and window positions of my EVE clients, I created this script which takes over this task for me.

## How it works
The scipt iterates through all configured EVE Online client profiles, scans for a file pattern and replaces the file content of all matched files to the one last modified.
The patterns it is looking for are:
```
core_user_*.dat
core_char_*.dat
```

## Requirements
* Python

## WARNING
Keep in mind: The settings of the last logged in char will overwrite the settings of all other chars found within each profile!
I advise to log in a considered "ready to copy" Char with all settings made, before running the script.

## Usage:
1. Copy the attached file to any directory
2. Adjust the variable ```profileBasePath``` within the file to the profile path of the EVE Online client.
This is usually:\
```C:\Users\<your user name>\AppData\Local\CCP\EVE\c_ccp_eve_online_tq_tranquility``` (remember to escape backslash)
4. Enter the names of your profiles which should be synced to the array variable ```profileNames```
5. Read the warning again
6. Run the file

If the script is useful for you, feel free to donate some ISK to "Xar'gal"
