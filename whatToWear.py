import requests

from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
#this file is built for my own use but all variables and acoounts can be changed to your own
#just use task chedluer to have this run whenever you want it too




def readWeather():
    res = requests.get("https://api.weather.gov/points/32.6085,-85.4834")
    response = res.json()
    hourly = response['properties']['forecastHourly']
    hour = requests.get(f"{hourly}")
    hourAPI = hour.json()
    return hourAPI

#could make it so timeframe is adjustable
def avgTemp():
    hour = readWeather()
    comb = 0
    for x in range(12):
        comb = comb + int(hour['properties']['periods'][x]['temperature'])
    return float(comb / 12)


#this costs money to run! (this does not work I am not paying monthly fees, but if i ever wanted to all i would need to do is host it)
def text():
    #put your info in here(twilio info)
    sid = ""
    token = ""
    phoneNum = ""
    yourPhone = ""
    
    client = Client(sid,token)
    mess = client.messages \
        .create(
            body='',
            from_ = phoneNum,
            to = yourPhone
        )
    return mess
    
#since dont want money to send texts will just email my phone
def email(body,password):
    sender ="rolliepollie1110@gmail.com"
    recipient = "justind1110@hotmail.com"
    msg = MIMEText(body)
    msg['Subject'] = "what to wear"
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")
    

def CurTemp():
    hour = readWeather()
    return hour['properties']['periods'][0]['temperature']

'''
def rainy():
    response = requests.get("https://api.weather.gov/points/32.6085,-85.4834")
    return str(response)
    '''

def rainy():
    res = requests.get("https://api.weather.gov/points/32.6085,-85.4834")
    response = res.json()
    forcas = response['properties']['forecast']
    forc = (requests.get(forcas)).json()
    chance =str(forc['properties']['periods'][0]['probabilityOfPrecipitation']['value'])
    if(chance == None): chance = "0"
    return str(str(forc['properties']['periods'][0]['shortForecast'])+ "\nPercent of Rain: " + chance)
    

def top():
    if( CurTemp() > 100): return "do not go outside to hot"
    if( CurTemp() > 75): return "tshirt"
    if(CurTemp() > 60 and float(avgTemp()) > float(65) and rainy() != False): return "tshirt"
    if(CurTemp() > 50 and avgTemp() < float(65) and rainy() != False): return "longsleeve"
    if(avgTemp() > 35): return "sweater"
    return "do not go outside too cold"

def bottom():
    if( CurTemp() > 100): return "do not go outside to hot"
    if( CurTemp() > 50): return "shorts"
    if(avgTemp() > 35): return "pants"
    return "do not go outside too cold"

def combine():
    
    return("Current Temp: " + str(CurTemp()) + "\nAvg for next few hours: " + str(avgTemp()) + "\nTop: " + top() + "\nbottom: " + bottom() + "\nweather: " + rainy())
    
    
    

def main():
    
    """"
    Temp = CurTemp()
    avg = avgTemp()
    top = top()
    
    time = datetime.now()
    
    location = "32.6085, -85.4834"
    
    text = "Do not \"rest your eyes\"\tCurrent Temp: {} average Temp: {}\tRecomended Top: {}\tRecomended Bottom: {}\tRecomended Umbrella: {}\tRecomended Shoes:{}".format(Temp,avg,top,bot,umb,shoe)
        
    
    print(text)
    """
    
    Temp =combine()
    print(Temp)
    #if you want to use you need your own password
    email(Temp, "wlnb oujp ghsk uhmz")
    
    #print(top())
main()
    
    
