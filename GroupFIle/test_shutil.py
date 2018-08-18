import shutil, os, zipfile
import send2trash

if __name__ == '__mian__':
    os.chdir('../TestPaper')
    shutil.copy('capitalsquize_answers1.txt', '././GroupFIle')
    shutil.copytree('capitalsquize_answers1.txt', './GroupFile')
    shutil.move('capitalsquize_answers1.txt', './GroupFile')
    # 删除
    # os.unlink(filename)
    send2trash.send2trash('bacon.txt')
    # 遍历目录树
    for foldername, subfolders, filenames in os.walk('./'):
        print(foldername)
    #zipfile
    exampleZip = zipfile.ZipFile('example.zip')
    exampleZip.namelist()
    spaminfo = exampleZip.getinfo('spam.txt')
    spaminfo.file_size
    exampleZip.extractall()
    exampleZip.close()
    newzip = zipfile.ZipFile('new.zip', 'w')
    newzip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    