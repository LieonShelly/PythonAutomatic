import webbrowser
import sys
import requests
import bs4
import os

def test():
    print('Googling')
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select('.r a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))



def downloadCartoon():
    url = 'http://xkcd.com/'
    os.makedirs('xkcd', exist_ok=True)
    while not url.endswith('#'):
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        comicElem = soup.select('#commic img')
        if comicElem == []:
            print('Could not find commic image')
        else:
            commicUrl = 'http:' + comicElem[0].get('src')
            print('Downloading image %s ...' % (commicUrl))
            res = requests.get(commicUrl)
            res.raise_for_status()
            imagefile = open(os.path.join('xkcd', os,path.basename(commicUrl)), 'wb')
            print(os.path.join('xkcd', os,path.basename(commicUrl)))
            for chunk in res.iter_content(10000):
                imagefile.write(chunk)
            imagefile.close()
        prevLink = soup.select('a[rel = "prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get(url)

    print('Done')



if __name__ == '__main__':
    downloadCartoon()