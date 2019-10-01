import os, shutil
import re

#Import Necessary libraries to operate the OS.

tsPath = ""
tsPathAC = "Z:\TABLET SCANNED PICS\CDAC\\"
tsDirAC = os.listdir(tsPathAC)
tsPathHO = "Z:\TABLET SCANNED PICS\CDHO\\"
tsDirHO = os.listdir(tsPathHO)
tsPathFL = "Z:\TABLET SCANNED PICS\CDFL\\"
tsDirFL = os.listdir(tsPathFL)
tsPathTR = "Z:\TABLET SCANNED PICS\CDTR\\"
tsDirTR = os.listdir(tsPathTR)
tsPathWR = "Z:\TABLET SCANNED PICS\CDWR\\"
tsDirWR = os.listdir(tsPathWR)

#Above - tsPath is used as a variable to hold the directory that a file should be redirected to.
#      - tsDirXX is used to define varying folders within the Tablet Scan Folder that a file can
#        be stored in.
#Further explained below.

mLPath = ""
mlPathAC = "Z:\MASTER ITEM NUMBER LIST\CDAC\\"
mlDirAC = os.listdir(mlPathAC)
mlPathHO = "Z:\MASTER ITEM NUMBER LIST\CDHO\\"
mlDirHO = os.listdir(mlPathHO)
mlPathFL = "Z:\MASTER ITEM NUMBER LIST\CDFL\\"
mlDirFL = os.listdir(mlPathFL)
mlPathTR = "Z:\MASTER ITEM NUMBER LIST\CDTR\\"
mlDirTR = os.listdir(mlPathTR)
mlPathWR = "Z:\MASTER ITEM NUMBER LIST\CDWR\\"
mlDirWR = os.listdir(mlPathWR)

#Above - mLPath is used as a variable to hold the directory that a master item picture should be redirected to.
#      - mlDirXX is used to define varying folders within the Master List Folder that a file can
#        be stored in.
#Further explained below.

iTPath = ""
itPathAC = "Z:\ITEM NUMBERED LIST FOR TAGGING\CDAC\\"
itDirAC = os.listdir(itPathAC)
itPathHO = "Z:\ITEM NUMBERED LIST FOR TAGGING\CDHO\\"
itDirHO = os.listdir(itPathHO)
itPathFL = "Z:\ITEM NUMBERED LIST FOR TAGGING\CDFL\\"
itDirFL = os.listdir(itPathFL)
itPathTR = "Z:\ITEM NUMBERED LIST FOR TAGGING\CDTR\\"
itDirTR = os.listdir(itPathTR)
itPathWR = "Z:\ITEM NUMBERED LIST FOR TAGGING\CDWR\\"
itDirWR = os.listdir(itPathWR)

#Above - iTPath is used as a variable to hold the directory that a item tagged picture should be redirected to.
#      - itDirXX is used to define varying folders within the Item Tagged Folder that a file can
#        be stored in.
#Further explained below.

filesToBeMoved = "Z:\DISCONTINUED FLORALS\\"                #Assigns the location to pull files from
moveToLocation = "Z:\DISCONTINUED FLORALS\\"                #Assigns the location to place located files (Images Only)
tsMoveToLocation = "Z:\DISCONTINUED FLORALS\PDF\\"          #Assigns the location to place located files (Tablet Scans Only)

dirs = os.listdir(filesToBeMoved)                           #Creates a list to loop through files in Files to be Moved
unfoundFiles = []                                           #Creates a list to append files that are not found in the source location

for file in dirs:                                                                   #Start Initial Loop
    try:
        fileName = re.search(r'(CD..[0-9][0-9][0-9][0-9])', file)                   #Initialize Regex definition - 4-Digit Sku
        fileName = fileName.group(1)                                                #Re-initialize as match found
    except AttributeError:
        try:
            fileName = re.search(r'(CD..[0-9][0-9][0-9])\D+\w.*', file)             #Initialize Regex definition - 3-Digit Sku
            fileName = fileName.group(1)                                            #Re-initialize as match found
        except AttributeError:
            try:
                fileName = re.search(r'(CD..[0-9][0-9])\D+\w.*', file)              #Initialize Regex definition - 2-Digit Sku
                fileName = fileName.group(1)                                        #Re-initialize as match found
            except AttributeError:
                print('')
                continue

    if "CDAC" in fileName:                                                      #If CDAC found in the filename,
        tsFileList = [x for x in tsDirAC if re.search(fileName, x)]             #For item in path, if a match for a regex search
        tsPath = tsPathAC                                                       #including the filename is found -->

    elif "CDHO" in fileName:                                                    #See Above, CDHO Variant
        tsFileList = [x for x in tsDirHO if re.search(fileName, x)]
        tsPath = tsPathHO

    elif "CDFL" in fileName:                                                    #See Above, CDFL Variant
        tsFileList = [x for x in tsDirFL if re.search(fileName, x)]
        tsPath = tsPathFL

    elif "CDTR" in fileName:                                                    #See Above, CDTR Variant
        tsFileList = [x for x in tsDirTR if re.search(fileName, x)]
        tsPath = tsPathTR

    else:                                                                       #See Above, CDWR Variant
        tsFileList = [x for x in tsDirWR if re.search(fileName, x)]
        tsPath = tsPathWR

    for i in tsFileList:                                                        #Start Secondary Loop, Through Tablet Scans Folder
        if len(fileName) <= 7:                                                  #If length of filename is < 7,
            try:
                newFile = re.search(r'(CD..[0-9][0-9][0-9])\D+\w.*', i)         #Set newFile = 3-Digit Regex Search, No Digit after 3rd
                newFile = newFile.group(0)                                      #Convert to string value of regex search
                try:
                    shutil.move(tsPath + newFile, tsMoveToLocation + newFile)   #Move to Tablet Scan Path determined by fileName
                    print("Moved : " + newFile + " to " + tsMoveToLocation)     #
                except FileNotFoundError:
                    print('[EXPECTED EXCEPTION] File Not Found In ' + iTPath + ' - Continuing..')
                    unfoundFiles.append(i)
                    continue
            except AttributeError:
                continue
        else:
            try:
                shutil.move(tsPath + i, tsMoveToLocation + i)                 #For Each Item, Find in TS Location, Move to Discontinued Folder
                print("Moved : " + i + " to " + tsMoveToLocation)
            except FileNotFoundError:
                print('[EXPECTED EXCEPTION] File Not Found In ' + iTPath + ' - Continuing..')
                unfoundFiles.append(i)


    if "CDAC" in fileName:
        mlFileList = [x for x in mlDirAC if re.search(fileName, x)]   #Initialize list matching skus pulled by Regex statement, Master List
        mLPath = mlPathAC
    elif "CDHO" in fileName:
        mlFileList = [x for x in mlDirHO if re.search(fileName, x)]
        mLPath = mlPathHO
    elif "CDFL" in fileName:
        mlFileList = [x for x in mlDirFL if re.search(fileName, x)]
        mLPath = mlPathFL
    elif "CDTR" in fileName:
        mlFileList = [x for x in mlDirTR if re.search(fileName, x)]
        mLPath = mlPathTR
    else:
        mlFileList = [x for x in mlDirWR if re.search(fileName, x)]
        mLPath = mlPathWR

    for i in mlFileList:                                            #Start Tertiary Loop
        if len(fileName) <= 7:
            try:
                newFile = re.search(r'(CD..[0-9][0-9][0-9])\D+\w.*', i)
                newFile = newFile.group(0)
                try:
                    shutil.move(mLPath + newFile, moveToLocation + newFile)
                    print("Moved : " + newFile + " to " + mLPath)
                except FileNotFoundError:
                    print('[EXPECTED EXCEPTION] File Not Found In ' + iTPath + ' - Continuing..')
                    unfoundFiles.append(i)
                    continue
            except AttributeError:
                continue
        else:
            try:
                shutil.move(mLPath + i, moveToLocation + i)                 #For Each Item, Find in ML Location, Move to Discontinued Folder
                print("Moved : " + i + " to " + moveToLocation)
            except FileNotFoundError:
                print('[EXPECTED EXCEPTION] File Not Found In ' + mLPath + ' - Continuing..')
                unfoundFiles.append(i)

    if "CDAC" in fileName:
        iTFileList = [x for x in itDirAC if re.search(fileName, x)]   #Initialize list matching skus pulled by Regex statement, Item Tagged List
        iTPath = itPathAC
    elif "CDHO" in fileName:
        iTFileList = [x for x in itDirHO if re.search(fileName, x)]
        iTPath = itPathHO
    elif "CDFL" in fileName:
        iTFileList = [x for x in itDirFL if re.search(fileName, x)]
        iTPath = itPathFL
    elif "CDTR" in fileName:
        iTFileList = [x for x in itDirTR if re.search(fileName, x)]
        iTPath = itPathTR
    else:
        iTFileList = [x for x in itDirWR if re.search(fileName, x)]
        iTPath = itPathWR

    for i in iTFileList:                                            #Start Quaternary Loop
        if len(fileName) <= 7:
            try:
                newFile = re.search(r'(CD..[0-9][0-9][0-9])\D+\w.*', i)
                newFile = newFile.group(0)
                try:
                    shutil.move(iTPath + newFile, moveToLocation + newFile)
                    print("Moved : " + newFile + " to " + moveToLocation)
                except FileNotFoundError:
                    print('[EXPECTED EXCEPTION] File Not Found In ' + iTPath + ' - Continuing..')
                    unfoundFiles.append(i)
                    continue
            except AttributeError:
                continue
        else:
            try:
                shutil.move(iTPath + i, moveToLocation + i)                 #For Each Item, Find in IT Location, Move to Discontinued Folder
                print("Moved : " + i + " to " + moveToLocation)
            except FileNotFoundError:
                print('[EXPECTED EXCEPTION] File Not Found In ' + iTPath + ' - Continuing..')
                unfoundFiles.append(i)

print(unfoundFiles)
