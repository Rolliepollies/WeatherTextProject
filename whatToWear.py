import requests
import datetime

def readWeather():
    response = requests.get("https://api.weather.gov/points/32.6085,-85.4834")
    hourly = response['properties']['forecastHourly']
    hourAPI = requests.get(f"{hourly}")
    return hourAPI
def avgTemp():
    hour = readWeather()
    allTemps = list
    comb = int
    for x in range(12):
        allTemps.append(hour['properties']['periods']['properties']['{x}']['temperature'])
    for y in allTemps:
        comb = comb + y
    return comb / 12

def CurTemp():
    hour = readWeather()
    return hour['properties']['periods']['properties']['1']['temperature']

def rainy():
    response = requests.get("https://api.weather.gov/points/32.6085,-85.4834")
    

def top():
    if( CurTemp() > 75): return "tshirt"
    if(CurTemp() > 60 & avgTemp() > 65 & rainy() != False): return "tshirt"
    

def main():
    
    
    Temp = CurTemp()
    avg = avgTemp()
    top = top()
    
    time = datetime.now()
    
    location = "32.6085, -85.4834"
    
    text = "Do not \"rest your eyes\"\tCurrent Temp: {} average Temp: {}\tRecomended Top: {}\tRecomended Bottom: {}\tRecomended Umbrella: {}\tRecomended Shoes:{}".format(Temp,avg,top,bot,umb,shoe)
        
    
    print(text)
    