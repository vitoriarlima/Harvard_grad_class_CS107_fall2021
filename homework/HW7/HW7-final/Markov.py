import numpy as np
import pandas as pd

class Markov():
    def __init__(self, day_zero_weather = None): # You will need to modify this header line later in Part C
        self.data = np.array([[]])
        self.weather_map = {'sunny': 0, 'cloudy': 1, 'rainy':2, 'snowy':3, 'windy':4, 'hailing': 5}
        self.day_zero_weather = day_zero_weather
        self.count = 0
        self._current_day_weather = day_zero_weather #None
        self.updated1 = day_zero_weather
        self.updated2 = day_zero_weather

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter = ",")

    def get_prob(self, current_day_weather, next_day_weather):
        current_day = current_day_weather.lower() #all lower case letters
        next_day = next_day_weather.lower()
              
        if current_day in self.weather_map.keys():
            i = self.weather_map.get(current_day)
            if next_day in self.weather_map.keys():
                j = self.weather_map.get(next_day)
            else:
                raise Exception("Next Day Weather not in list of weather")         
        else:
            raise Exception("Current Day Weather not in list of weather")
            
        return self.data[i][j]
    
    def __iter__(self):
        return MarkovIterator(self, self.today)
    
    
    def _simulate_weather_for_day(self,day):
        '''Need to get weather for day specified to add'''
        if day == 0 :
            return self._current_day_weather
        elif day > 0:
            self.updated1 = self.day_zero_weather
            self.count = 0 
            while self.count <= day:
                # once next function works 
                #print("one",self.updated1 )
                self.updated2 = next(iter(MarkovIterator( self, self.updated1 ))) #._current_day_weather)
                #print("UPDATED TWO",self.updated2 )
                #print("two",self.updated2)
                self.updated1 =  self.updated2 
                #print("updated one",self.updated1 )
                self.count += 1
                self.updated2 

            #should give us the weather of the correct day 
            return self.updated2   #self.updated2
        else: 
            raise ValueError("Day must be non negative")

    def get_weather_for_day(self, day=3, trials = 100):
        '''List of weather for the specified day and done a certain amount of trials'''
        i = 0
        weather_list = []
        
        
        while i < trials: 
            weather_list.append(self._simulate_weather_for_day(day))
            i += 1
        return weather_list
         
    

class MarkovIterator:
    def __init__(self, m: Markov, day_zero_weather):
        self.m = m
        self.today = day_zero_weather
        self.count_next = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.today in self.m.weather_map.keys():
            index = self.m.weather_map.get(self.today)
            row = self.m.data[index, :]
            #print(row)
            tomorrow_state = np.random.choice(6, 1, p = row)
            val = tomorrow_state[0]

            for weather, index in self.m.weather_map.items():
                if val == index:
                    self.today = weather
                    self.count_next +=1
                    return self.today
        else:
            raise Exception("Current Day is not in list of weather")

       