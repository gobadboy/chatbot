import os
from twilio.rest import Client


client = Client()

account_sid: str = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_whatsapp_number = 'whatsapp: +14155238886',
to_whatsapp_number = 'whatsapp: +9499030158',
client.message.create(body='hi you have registered',
                      from_=from_whatsapp_number,
                      to=to_whatsapp_number)