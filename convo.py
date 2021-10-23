

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  




with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as fin:
    raw = fin.read().lower()

# TOkenisation
sent_tokens = nltk.sent_tokenize(raw)  
word_tokens = nltk.word_tokenize(raw)  

# Preprocessing
lemmer = WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


flag = True
print("ROBO: My name is Robo cpo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while (flag == True):
    user_response = input()
    user_response = user_response.lower()
    if (user_response != 'bye'):
         if (user_response == 'thanks' or user_response == 'thank you' or user_response== 'end'):
            flag = False
            print("ROBO: You are welcome..")
        else:
            if (greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                print("ROBO: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("ROBO: Bye! take care..")

        if (user_response == 'Cyber crime awareness' or user_response == 'cyber crime awareness'):
            print(
                'Cybercrime is a crime that involves a computer and a network.Cybercrime may harm someones security and '
                'financial health.Cybercrimes crossing international borders and involving the actions of at least one '
                'nation-state are sometimes referred to as cyberwarfare.Lack of user awareness about Internet, cyber laws '
                'and risks pose a big challenge in India.')

        elif (user_response == 'Criminal crime awareness' or user_response == 'criminal crime awareness'):
            print('the intentional commission of an act usually deemed socially harmful or dangerous and specifically '
                  'defined, prohibited, and punishable under criminal law.For example, many legal systems take into account '
                  'the mental state of the accused person at the time the alleged crime was committed.')

        elif (user_response == 'Robbery crime awareness' or user_response == 'robbery crime awareness'):
            print('Robbery is the crime of taking or attempting to take anything of value by force, threat of force, '
                  'or by putting the victim in fear.Robbery is differentiated from other forms of theft (such as burglary, '
                  'shoplifting, pickpocketing, or car theft) by its inherently violent nature (a violent crime); whereas many '
                  'lesser forms of theft are punished as misdemeanors, robbery is always a felony in jurisdictions that '
                  'distinguish between the two.')

        elif (user_response == 'Civil crime awareness' or user_response == 'civil crime awareness'):
            print('Civil crime deals with behavior that constitutes an injury to an individual or other private party, '
                  'such as a corporation. Examples are defamation including libel and slander, breach of contract, '
                  'negligence resulting in injury or death, and property damage.Examples are murder, assault, theft,and drunken '
                  'driving.')
       



