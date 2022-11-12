import requests
api_key = '9f841ce9c76ce68dba34edc4efa45493'
def get_data(city, days=None, fc_type=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    print(get_data('London'))



