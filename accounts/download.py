#forego run python3 download.py argv

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os,time,sys

KEY = os.environ['FLICKR_KEY']
SECRET_KEY = os.environ['FLICKR_SECRET_KEY']
WAITTIME = 1

try:
    searchText = sys.argv[1]
except:
    print('put any text you want to get as "argv"')
    raise IndexError

saveDir = "./" + searchText
if not os.path.exists(saveDir):
    os.mkdir('./'+searchText)

flickr = FlickrAPI(KEY,SECRET_KEY,format='parsed-json')
result = flickr.photos.search(
    text = searchText,
    per_page = 20,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q,licence'
)

photos = result['photos']

for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = saveDir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):continue
    urlretrieve(url_q,filepath)
    time.sleep(WAITTIME)

