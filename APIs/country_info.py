import requests
import json

def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.com/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def get_country_code(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['alpha3Code']
    return None

def get_country_currency(countries: list, country_name: str):
    for country in countries:
        if country['name'] == country_name:
            return country['currencies'][0]['code']
    return None

def transform(name: str):
    countries = get_countries()
    code = get_country_code(countries, name)
    currency = get_country_currency(countries, name)

    return {"name": name, "country_code": code, "currency_code": currency}

def display_countries():
    idx = 0
    countries = get_countries()

    for country in countries:
        print(idx, country['name'])
        idx += 1

    return countries

def show_country_info():
    countries = display_countries()
    
    selected_country_idx = int(input("Please choose a country: "))
    
    name = countries[selected_country_idx]['name']
    result = transform(name)
    print(result)
    
show_country_info()
