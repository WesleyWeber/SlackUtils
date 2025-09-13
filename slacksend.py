#!/usr/bin/python3
import os
import configparser
import sys
import slack_sdk

CONFIG = configparser.ConfigParser()
CONFIG.read('slacksend.conf')

TOKEN = CONFIG['SLACKSEND']['TOKEN']
CHAN = CONFIG['SLACKSEND']['CHAN']
ERROR_MSG = CONFIG['SLACKSEND']['ERROR']

SLACK_C = slack_sdk.WebClient(token=TOKEN)


try:
    chan = sys.argv[1]
except IndexError as e:
    chan = CHAN
    os.system("logger \"$0 error decoding channel for slacksend at `date`\"")

try:
    msg = sys.argv[2] 
except IndexError as e:
    msg = ERROR_MSG
    os.system("logger \"$0 error decoding message for slacksend at `date`\"")

try:
    response = SLACK_C.chat_postMessage(channel=chan, text=msg)
    os.system("logger \"$0 sent slack msg ({}@{}) at `date`\"".format(chan,msg))
except Exception as e:
    print(e)