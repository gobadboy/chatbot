from app import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pathlib
from twilio.rest import Client

if crime == 'Cyber crime awareness':
    print('Cybercrime is a crime that involves a computer and a network.Cybercrime may harm someones security and '
          'financial health.Cybercrimes crossing international borders and involving the actions of at least one '
          'nation-state are sometimes referred to as cyberwarfare.Lack of user awareness about Internet, cyber laws '
          'and risks pose a big challenge in India.')

elif crime == 'Criminal crime awareness':
    print('the intentional commission of an act usually deemed socially harmful or dangerous and specifically '
          'defined, prohibited, and punishable under criminal law.For example, many legal systems take into account '
          'the mental state of the accused person at the time the alleged crime was committed.')

elif crime == 'Robbery crime awareness':
    print('Robbery is the crime of taking or attempting to take anything of value by force, threat of force, '
          'or by putting the victim in fear.Robbery is differentiated from other forms of theft (such as burglary, '
          'shoplifting, pickpocketing, or car theft) by its inherently violent nature (a violent crime); whereas many '
          'lesser forms of theft are punished as misdemeanors, robbery is always a felony in jurisdictions that '
          'distinguish between the two.')

elif crime == 'Civil crime awareness':
    print('Civil crime deals with behavior that constitutes an injury to an individual or other private party, '
          'such as a corporation. Examples are defamation including libel and slander, breach of contract, '
          'negligence resulting in injury or death, and property damage.Examples are murder, assault, theft,and drunken '
          'driving.')

else:
    print("crime is not found")

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
