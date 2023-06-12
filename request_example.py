import json
import urllib.request

# urlData = 'https://api.coinbase.com/v2/exchange-rates?currency=USD'
urlData = 'https://randomuser.me/api/?results=' + input("Cuantos quieres? ")

webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
JSON_object = json.loads(data.decode(encoding))
print(JSON_object)
