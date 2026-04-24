import urllib.request
import re

url = "https://www.pexels.com/search/videos/tailor/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    urls = re.findall(r'https://videos\.pexels\.com/video-files/[^\"\' ]+', html)
    print(urls[0] if urls else "none")
except Exception as e:
    print(e)
