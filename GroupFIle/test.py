import shutil, os, re

def text:
    datePattern = re.compile(r"""^(.?)
    ((0|1)?\d) -
    ((0|2|3)?\d) -
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)
    for amerfilename in os.listdir('.')
        mo = datePattern.search(amerfilename)
        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        datPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        euroFilename = beforePart + datPart + '-' + monthPart + '-' + yearPart + afterPart
        absWorkingDir = os.path.abspath('.')    
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)
        
