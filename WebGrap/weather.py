import json, requests, sys

def index():
    if(len(sys.argv) < 2):
        print('usage: quickWeather.py location')
    location = ' '.join(sys.argv[1: ])
    url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
    response = requests.get(url)
    response.raise_for_status()
    wetherData = json.loads(response.text)
    

if __name__ == '__main__':
    index()