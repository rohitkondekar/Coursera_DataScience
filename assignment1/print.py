import urllib
import json

response = urllib.urlopen("https://api.twitter.com/1.1/search/tweets.json?q=anshawe")
o = json.load(response)
print o


