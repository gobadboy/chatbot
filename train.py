from app import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pathlib
from twilio.rest import Client

account_sid: str = "ACf10b182ce5503450fdb93e992f1eab97"
auth_token = "fc6c33f6e908f66e6102ce90bd8992cd"

client = Client(account_sid , auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919499030158'
message = client.messages.create(from_=from_whatsapp_number,
                             to=to_whatsapp_number,
                            body='hi this is venki')
print(message.sid)


trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    str(pathlib.Path().absolute())+'/english/',
)
