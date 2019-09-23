import os, shutil
import re

tsPath = "C:\\Users\Carol\Desktop\TSRemove\Tablet Scanned\\"
tsDir = os.listdir(tsPath)                                      #Create List of Tablet Scan Folder

mLPath = "C:\\Users\Carol\Desktop\TSRemove\Master Item\\"
mlDir = os.listdir(mLPath)                                      #Create List of Master Item Number Folder

iTPath = "C:\\Users\Carol\Desktop\TSRemove\Item Numbered\\"
itDir = os.listdir(iTPath)                                      #Create List of Item Number Tagged Folder

filesToBeMoved = "C:\\Users\Carol\Desktop\TSRemove\Files To Move\\"     #Assign the location to pull files from
moveToLocation = "C:\\Users\Carol\Desktop\TSRemove\Move Location\\"     #Assign the location to place fulled files

dirs = os.listdir(filesToBeMoved)

for file in dirs:                                               #Start Initial Loop
    fileName = re.search(r'(CD..[0-9][0-9][0-9][0-9])', file)       #Initialize Regex definition - 4-Digit Sku
    fileName = fileName.group(1)                                    #Re-initialize as match found

    tsFileList = [x for x in tsDir if re.search(fileName, x)]   #Initialize list matching skus pulled by Regex statement, Tablet Scans
    for i in tsFileList:                                            #Start Secondary Loop
        shutil.move(tsPath + i, moveToLocation + i)                 #For Each Item, Find in TS Location, Move to Discontinued Folder
        print("Moved : " + i + " to " + tsPath)

    mlFileList = [x for x in mlDir if re.search(fileName, x)]   #Initialize list matching skus pulled by Regex statement, Master List
    for i in mlFileList:                                            #Start Tertiary Loop
        shutil.move(mLPath + i, moveToLocation + i)                 #For Each Item, Find in ML Location, Move to Discontinued Folder
        print("Moved : " + i + " to " + mLPath)

    iTFileList = [x for x in itDir if re.search(fileName, x)]   #Initialize list matching skus pulled by Regex statement, Item Tagged List
    for i in iTFileList:                                            #Start Quaternary Loop
        shutil.move(iTPath + i, moveToLocation + i)                 #For Each Item, Find in IT Location, Move to Discontinued Folder
        print("Moved : " + i + " to " + iTPath)
    #print(mlDir)
    #print(itDir)
    #print(tsDir)
