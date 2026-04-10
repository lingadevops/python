#API
#https://www.yelp.com/v3/businesses/search
import requests
import config
URL = 'https://api.yelp.com/v3/businesses/search'
API_KEY = config.API_KEY
params = {
    'location': 'San Francisco',
    'term': 'restaurants'
}
response = requests.get(URL, headers={'Authorization': 'Bearer ' + API_KEY}, params=params)

businesses = response.json().get('businesses')
names = [business['name'] for business in businesses]
print(names)