from sqlconnectivity import *
from weather import *
from translate import *
from speak import *
from send_msg import *

def message_built():
    user_data = view_all()
    for user in user_data:
        mobile_num = user[0]
        city = user[1]
        name = user[2]
        print(mobile_num,city,name)
        weather_report1 = weather_finder(city)
        #print(weather_report1)
        for weather_report in weather_report1:
            time= weather_report[0]
            date = weather_report[1]
            description = weather_report[2]
            temp=weather_report[3]
            message_construct = messege_creation(name,city,date,description,temp,time)
            message_construct = convert_into_hindi(message_construct)
            print(message_construct)
            #speak(message_construct,name,date)
            #send_message(mobile_num,message_construct)

message_built()