import builder
import generator
import random
from TwitterAPI import TwitterAPI
from functools import *
import json
consumer_key= ""
consumer_secret= ""
access_token_key= ""
access_token_secret= ""


def randomizer(bound):
    return random.randint(1, bound)

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

r = api.request('statuses/user_timeline', {'screen_name': "MarcoRubio", 'count': 200}).json()
t = api.request('statuses/user_timeline', {'screen_name': "realDonaldTrump", 'count': 200}).json()
sanders = api.request('statuses/user_timeline', {'screen_name': "sensanders", 'count': 200}).json()
clinton = api.request('statuses/user_timeline', {'screen_name': "HillaryClinton", 'count': 200}).json()
lahren = api.request('statuses/user_timeline', {'screen_name': "tomilahren", 'count': 200}).json()
subaru = api.request('statuses/user_timeline', {'screen_name': "sadieisonfire", 'count': 200}).json()
barack = api.request('statuses/user_timeline', {'screen_name': "barackobama", 'count': 200}).json()
meme = api.request('statuses/user_timeline', {'screen_name': "billratchet", 'count': 200}).json()

List = [t]
flattenedList = list(map(lambda x: "&" if x == "&amp;" else x, filter(lambda z: not "http" in z and not "RT" in z and not "@" in z, reduce(lambda x, y: x+" "+y, [elem['text'] for item in List for elem in item]).split())))
#print(flattenedList)

randomInt = randomizer(len(flattenedList) - 4)
randomSelection = flattenedList[randomInt:randomInt+3]

with open("Output.txt", "w", encoding='utf-8') as text_file:
    for item in randomSelection:
        text_file.write(item + " ")
    for item in flattenedList:
        text_file.write(item + " ")

    # lst = None
    # lstRando = None
    # with open("Output.txt", encoding='utf-8') as file:
    #     lst = file.read().split()
    #     lstRando = lst[78:81]
    #     #print (lstRando)

    # with open("Output.txt", "w", encoding='utf-8') as text_file:
    #     text_file.seek(0, 0)
    #     reducedLst = reduce(lambda x, y: x+" "+y, lst)
    #     reducedLstRando = reduce(lambda x, y: x+" "+y, lstRando)
    #     #print(reducedLst)
    #     #print(reducedLstRando)
    #     text_file.write(reducedLstRando + " " + reducedLst)


file_name = 'Output.txt'
chain = builder.build(file_name)
num_words = 20
outstr = generator.generate(chain, randomizer, num_words, builder.NONWORD)
api.request("statuses/update", {'status': outstr})
print(outstr)
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
print("****************************************")
