import zipfile, os

def backuptoZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        print('Creating %s....' % (zipFilename))
        backupZip = zipfile.ZipFile(zipFilename, 'w')
        for foldername, subfolders, filenames in os.walk(folder)：
            print('Adding files in %s...' % (foldername))
            backuptoZip.write(foldername)
            for filename in filenames：
                newBase = os.path.basename(folder) + '_'
                if filename.startswitch(newBase) and filename.endswith('.zip')
                    continue
                backuptoZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('Done.')