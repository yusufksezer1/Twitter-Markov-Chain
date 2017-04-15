import builder
import generator
import random
from TwitterAPI import TwitterAPI
from functools import *
import time
import json

# Necessary TwitterAPI keys to post Tweets as @Robot_Rubio_
consumer_key= "TCMXtnTY1MnS28Hxfq8WVQ09E"
consumer_secret= "GZUNZD2Yo0ZdtjvjFdgfzAJ7XC3GA5HXvjv1w13iF43iBWy7sT"
access_token_key= "853011873490501632-adIZudaCei1LenZepfNHmyTPJLlWMm9"
access_token_secret= "esNuRlVrBZpS1o17w3K71sAwR4b7jlvPQ9VQrGRmW1rzu"


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
# Retrieves 200 Tweets per iteration for a total of 3200 Tweets
'''
List = []
lastID = None
for i in range(0, 15):
    t = api.request('statuses/user_timeline', {'screen_name': "realDonaldTrump", 'count': 200, "max_id": lastID})
    iter = t.get_iterator()
    last = [tweet for tweet in iter][-1]
    lastID = last['id']
    List += [t.json()]

# Flattens List so that we have one list of all the words from Trump's most-recent 3200 tweets
# Filters out retweets, mentions and links
# Fixes encoding issue where '&' are being read as '&amp'
# Please excuse disgusting one-liner
flattenedList = list(map(lambda x: "&" if x == "&amp;" else x, filter(lambda z: not "http" in z and not "RT" in z and not "@" in z, reduce(lambda x, y: x+" "+y, [elem['text'] for item in List for elem in item]).split())))

# Randomly selects three words from Trump's Tweets to write to the beginning of the file
# Our Markov Chain uses the first three words of the file to create the initial prefix-suffix pair
# This ensures that each Markov-Generated Tweet starts with different words
randomInt = randomizer(len(flattenedList) - 4)
randomSelection = flattenedList[randomInt:randomInt+3]

# Write our randomly selected 3 words to a .txt file
# Then write all of the text from the Tweets we retrieved earlier
with open("Output.txt", "w", encoding='utf-8') as text_file:
    for item in randomSelection:
        text_file.write(item + " ")
    for item in flattenedList:
        text_file.write(item + " ")


# Generate the new Tweet and post it to the @Robot_Rubio_ Twitter account
file_name = 'Output.txt'
chain = builder.build(file_name)
num_words = 20
outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
api.request("statuses/update", {'status': outstr})
print(outstr)
print("*****************SUCCESS!***********************")

