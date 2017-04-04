import requests

r = requests.get('http://espressotg.com/eotg/api/coffeeTypes/1')
print(r.text)
print(r.json())
