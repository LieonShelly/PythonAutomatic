import time
import datetime
import requests
from bs4 import BeautifulSoup

def index():
    input()
    print('statrted')
    startTime = time.time()
    lastTime = startTime
    lapNum = 1
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totlaTime = round(time.time() - startTime, 2)
            print('Lap #%s (%s)' % (lapNum, totlaTime, lapTime), end = " ")
            lapNum += 1
            lastTime = time.time()
    except KeyboardInterrupt:
        print('\nDone.')

def testDateTime():
    now = datetime.datetime.now()
    dt = datetime.datetime(2018, 10, 21, 16,29,0)
    print(dt.day)
    print(dt.hour)
    print(dt.minute)
    date = datetime.datetime.fromtimestamp(100000000)
    delta = datetime.timedelta(day=11, hours = 10, minute = 9, seconds = 8)
    delta.days
    delta.seconds
    delta.microseconds



def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get(' http://xkcd.com/%s...' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        commicElem = soup.select('#comic img')
        if commicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = commicElem[0].get('src')
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        downloadThreads = []
        for i in range(0, 1400, 100):
            downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99)
            downloadThreads.append(downloadThread)
            downloadThread.start()
        for downloadThread in downloadThreads:
                 downloadThread.join()
             print('Done.')
    



if __name__ == '__mian__':
    index()