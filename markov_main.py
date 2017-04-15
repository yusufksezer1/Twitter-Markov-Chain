import builder
import generator
import random
from TwitterAPI import TwitterAPI
from functools import *
import time
import json

# Necessary TwitterAPI keys, use keys linked to the account which you want to post Tweets to
consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''


def randomizer(bound):
    return random.randint(1, bound)

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

'''
# ***Workaround for TwitterAPI's 200 Tweets per request limit***
# Request 200 Tweets with the TwitterAPI
# Record the ID of the last Tweet retrieved from the request
# Pass the ID as a parameter in the next request to get the next 200 tweets
# Retrieves 200 Tweets per iteration for a total of 3200 Tweets (half from Trump, half from Rubio)
'''
List = []
tLastID = None
#rLastID = None
for i in range(0, 15):
    t = api.request('statuses/user_timeline', {'screen_name': "realDonaldTrump", 'count': 200, "max_id": tLastID})
    #r = api.request('statuses/user_timeline', {'screen_name': "marcorubio", 'count': 200, "max_id": rLastID})
    tLastID = t.response.json()[-1]['id']
    #rLastID = r.response.json()[-1]['id']
    #List += [t.json()] + [r.json()]
    List += [t.json()]

'''
# Flattens List so that we have one list of all the words from Trump's most-recent 3200 tweets
# Filters out retweets, mentions and links
# Fixes encoding issue where '&' are being read as '&amp'
# Please excuse disgusting one-liner
'''
flattenedList = list(map(lambda x: "&" if x == "&amp;" else x, filter(lambda z: not "http" in z and not "RT" in z and not "@" in z, reduce(lambda x, y: x+" "+y, [elem['text'] for item in List for elem in item]).split())))

'''
# Randomly selects three words from Trump's Tweets to write to the beginning of the file
# Our Markov Chain uses the first three words of the file to create the initial prefix-suffix pair
# This ensures that each Markov-Generated Tweet starts with different words
'''
randomInt = randomizer(len(flattenedList) - 4)
randomSelection = flattenedList[randomInt:randomInt+3]

'''
# Write our randomly selected 3 words to a .txt file
# Then write all of the text from the Tweets we retrieved earlier
'''
with open("Output.txt", "w", encoding='utf-8') as text_file:
    for item in randomSelection:
        text_file.write(item + " ")
    for item in flattenedList:
        text_file.write(item + " ")


# Generate the new Tweet and post it to the Twitter account linked to the TwitterAPI keys
file_name = 'Output.txt'
chain = builder.build(file_name)
num_words = 20
outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
api.request("statuses/update", {'status': "*Based off Trump Tweets*: " + outstr})
print(outstr)
print("*****************SUCCESS!***********************")