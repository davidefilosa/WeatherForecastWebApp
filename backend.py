import requests
api_key = '9f841ce9c76ce68dba34edc4efa45493'


def get_data(city, days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr = (8*days)
    filtered_data = filtered_data[:nr]
    return filtered_data


if __name__ == '__main__':
    print(get_data('London', 2, 'Temperature'))



