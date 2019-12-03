import requests
from  sqlconnectivity import *
from datetime import date as dt

def message_format(name,city,date,description,temp,time):
    message = "Hello "+name +","+ date +" "+ time +" Climate condition such as " + description+" in "+city+" ."
    return message

def messege_creation(name,city,date,description,temp,time):
    description = description.lower()
    if "clear" in description or "sky" in description:
        description = "The sky is clear and it's good weather for farming\n"
        message = message_format(name,city,date,description,temp,time)

    elif "clouds" in description or "cloud" in description:
        description = "the sky is cloudy and it's not good weather for farming\n "
        message = message_format(name,city,date,description,temp,time)

    elif "rain" in description or "raining" in description:
        description = "It's highly probablity for the raining so, get all the grains from feild\n"
        message = message_format(name,city,date,description,temp,time)

    elif "thunderstorm" in description:
        description = "it's thunderstorm , very high possibility of raining and high wind \n"
        message = message_format(name,city,date,description,temp,time)

    else:
        description = "bad weather\n"
        message = message_format(name,city,date,description,temp,time)

    return message

def weather_finder(city):

    api_key = 'your_api_key'
    api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key

    api_call += '&q=' + city

    json_data = requests.get(api_call).json()
    #print(json_data)

    location_data = {
            'city': json_data['city']['name'],
            'country': json_data['city']['country']
    }

    #print('\n{city}, {country}'.format(**location_data))
    today_date = str(dt.today())
    #print(today_date)
    year, month, day = today_date.split('-')
    if len(str(int(day)+2))!= 2:
        day = "0" + str(int(day) + 2)
    else:
        day = str(int(day) + 2)
    #print(day)
    day_list = [year,month,day]
    new_date = "-".join(day_list)
    #print(new_date)

    data = []

    for item in json_data['list']:
        time = item['dt_txt']
        next_date, hour = time.split(' ')

        if new_date == next_date:
            year, month, day = new_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
           # print('\n{m}/{d}/{y}'.format(**date))

        hour = int(hour[:2])
        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        if hour== 6 and new_date == next_date:
            #print('\n%i:00 %s' % (hour, meridiem))
            temperature = item['main']['temp'] - 273.15
            temperature = str(temperature)[:5]

            description = item['weather'][0]['description']

            #print('Weather condition: %s' % description)
            #messege_creation(description)
            #print('Celcius: {:.2f}'.format(temperature - 273.15))

            list = []
            list.append(str(hour)+meridiem)
            list.append(new_date)
            list.append(description)
            list.append(temperature)
            data.append(list)

    return data
#print(weather_finder("delhi"))