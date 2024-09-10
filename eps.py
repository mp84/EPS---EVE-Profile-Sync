import os
import re

def main():

    # EVE Profile Base Path
    profileBasePath = 'C:\\Users\\<your_username>\\AppData\\Local\\CCP\\EVE\\c_ccp_eve_online_tq_tranquility'

    # Installed profiles
    profileNames = ['settings_Default', 'settings_Potao', 'settings_whatever']

    # RegExp Patterns for file matching
    regexChar = re.compile(r'^core_char_\d+\.dat$')
    regexAccount = re.compile(r'^core_user_\d+\.dat$')

    printBanner(profileBasePath)

    for profileName in profileNames:
        fullProfilePath = os.path.join(profileBasePath, profileName)
    
        # Check if profile directory exists
        if not os.path.isdir(fullProfilePath):
            print(f"!!! Error: Profile {profileName} not found")
            continue

        print(f"Updating profile: {profileName}")

        # Generate list of files which match pattern
        fileListChar = [os.path.join(fullProfilePath, f) for f in os.listdir(fullProfilePath) if regexChar.match(f)]
        fileListAccount = [os.path.join(fullProfilePath, f) for f in os.listdir(fullProfilePath) if regexAccount.match(f)]

        # Update files for chars
        updateFiles(fileListChar)

        # Update files for account
        updateFiles(fileListAccount)

    print("")   
    print("done.")
    print("")
    input("Press enter to exit")



def printBanner(basePath):
    print(f"*** EPS - EVE Profile Sync by Xar'gal ***")
    print(f"")
    print(f"Configured profileBasePath: {basePath}")
    print(f"")



def updateFiles(fileList):
    if not fileList:
        print(f"!!! Error: File list is empty")
        return

    # Get file with latest changes
    latest_file = max(fileList, key=lambda f: os.path.getmtime(f))

    try:
        # Read binary content
        with open(latest_file, 'rb') as file:
            latest_content = file.read()
    except Exception as e:
        print(f"!!! Error: Reading {latest_file}: {e}")
        return

    # Update all files with latest content
    for file in fileList:
        if file != latest_file:  # Don't override source
            try:
                with open(file, 'wb') as f:
                    f.write(latest_content)
                    #print(f"OK")
            except Exception as e:
                print(f"!!! Error: Writing file {file}: {e}")
                continue

if __name__ == '__main__':
    main()
