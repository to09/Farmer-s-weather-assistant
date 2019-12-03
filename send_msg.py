from twilio.rest import Client

def send_message(mobile_number,message):
    account_sid = 'XXXXXXXXXX'
    auth_token = 'XXXXXXXXXX'
    mobile_number = "+91"+ mobile_number
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
                body=message,
                from_='Your_number',
                to= mobile_number
             )

    print(message.sid)
#send_message("9694057061","hello how are you")