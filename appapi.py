import requests
import json
from flask import jsonify
from bs4 import BeautifulSoup
BASE_URL = 'https://sinoptik.ua/' 
    
Headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36','accept': '*/*'}
   # "Host='https://explorer.cardano.org'"
    
#def Parser(city,type_):

def get_html(url, params=None):
    r = requests.get(url, headers=Headers, params=params)
    return r
   
def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    
    items = soup.find('div',id ='blockDays').find_all('div',class_='main')
    info={}
    info['weather'] = []
    for item in items:
        info['weather'].append({
            'day': item.find(class_='day-link').getText(),
            'date':  item.find(class_='date').getText(),
            'month': item.find(class_='month').getText(),
            'min': item.find(class_='min').span.getText(),
            'max': item.find(class_='max').span.getText(),
            })
    return (info)
    #return(json.dumps(info))
    #print(info)
    #print(len(item)  )
def get_content_all_cities(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find(id='weatherLinks').find_all('li')
    info = {}
    info['cities_weather'] = []
    for item in items:
        info['cities_weather'].append({
            'city2': item.a.get('title'),
            'temperature': item.find(class_='iw').getText(strip=True)
        })
    return (info)
def get_content_today(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find(id='weatherLinks').find_all('li')
    info = {}
    info['cities_weather'] = []
    for item in items:
        info['cities_weather'].append({
            'city2': item.a.get('title'),
            'temperature': item.find(class_='iw').getText(strip=True)
        })
    return (info)
def get_content_today(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find(class_='weatherDetails')
    #items_info_temperature = soup.find(class_='weatherDetails').find_all('tbody')
    info = {}
    headers = items.thead.find_all('td')
    times = items.tbody.find('tr', class_='time').findChildren('td')
    temperatures = items.tbody.find('tr', class_='temperature').findChildren('td')
    weetness = items.tbody.findChildren('tr')[5].findChildren('td')
    wind_speed = items.tbody.findChildren('tr')[6].findChildren('td')


    for idx, day_part in enumerate(headers):
        day_part_name = day_part.getText()
        info[day_part_name] = {
            times[idx*2].getText(): {
                'temperature': temperatures[idx*2].getText(),
                'weetness': weetness[idx*2].getText()
            }
        }

        info[day_part_name].update({
            times[idx * 2 + 1].getText(): {
                'temperature': temperatures[idx * 2 + 1].getText(),
                'weetness': weetness[idx * 2 + 1].getText()
            }
        })
        # info[day_part_name].append({
        #     'time': times[idx*2],
        #     'temperature':
        #
        #     # 'time': item.find_all(class_="gray time").find(class_='p1').getText(),
        #     # 'humidity': item.find(class_="gray time").find(class_='p1').getText(),
        #     # 'wind_speed': item.find_all(class_="gray").find(class_='p1').getText(),
        # })


    print(info)

    #print(items_info_temperature)
    '''
        info = {}
    info['cities_weather'] = []
    for item in items:
        info['cities_weather'].append({
            'city2': item.a.get('title'),
            'temperature': item.find(class_='iw').getText(strip=True)
        })
    return (info)

    '''





def getSevenDays(city):
    URL = BASE_URL + '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-' + city
    html = get_html(URL)
    if (html.status_code==200):
        return get_content(html.text)
    else:
        print("Error")
def getTenDays(city):
    URL = BASE_URL + '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-' + city +'/10-%D0%B4%D0%BD%D0%B5%D0%B9'
    html = get_html(URL)
    if (html.status_code==200):
        return get_content(html.text)
    else:
        print("Error")
def getAllCities():
    html = get_html(BASE_URL)
    if (html.status_code==200):
        return get_content_all_cities(html.text)
    else:
        print("Error")
def getToday(city):
    URL = BASE_URL + '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-' + city
    html = get_html(URL)
    if (html.status_code==200):
        return get_content_today(html.text)
    else:
        print("Error")
city = 'львов'
getToday(city)
'''
    result = {}
    result['weather'] = []
    for val in items:
        tmp = {}
        tmp['day'] = val.find(class_='day-link').getText()
        tmp['date'] = val.find(class_='date').getText()
        tmp['month'] = val.find(class_='month').getText()
        tmp['min'] = val.find(class_='min').span.getText()
        tmp['max'] = val.find(class_='max').span.getText()
        
        result['weather'].append(tmp)
    '''
'''
    def get_pages_count(html):
        soup = BeautifulSoup(html, 'html.parser')
        pagintation = soup.find_all('span',class_='Pagination_totalPagesNumber__2geNP')
        print(pagintation)
'''
        