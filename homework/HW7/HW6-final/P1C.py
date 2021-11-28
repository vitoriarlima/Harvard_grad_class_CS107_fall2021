from Markov import *

#https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
from collections import Counter
#Counter(z)

#https://stackoverflow.com/questions/16095220/can-you-make-counter-not-write-out-counter
import json 
#json.dumps

#https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
def most_common(lst):
    return max(set(lst), key=lst.count)


city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

print("Number of occurrences of each weather condition over the 100 trials for each city 7 days from the current day")
print("--------------------------------")
for key, value in city_weather.items():
    m = Markov(city_weather.get(key))
    #print(m)
    m.load_data(file_path='./weather.csv')
    my_list = m.get_weather_for_day( 7, 100 )
    sorted_list = Counter(my_list)
    sorted_list = json.dumps(sorted_list)
    #print(sorted_list)
    print(f"{key} : {sorted_list}") 

print(" ")
print(" ")
print("--------------------------------")
print("--------------------------------")
print(" ")
print(" ")

print("Most likely weather in seven days from the current day")
print("--------------------------------")
for key, value in city_weather.items():
    m = Markov(city_weather.get(key))
    #print(m)
    m.load_data(file_path='./weather.csv')
    my_list = m.get_weather_for_day( 7, 100 )
    #print(f"{key} today : {m.day_zero_weather} ") 
    #print(f"{key}, in seven days:{most_common(my_list)}") 
    print(f"{key}: {most_common(my_list)}") 