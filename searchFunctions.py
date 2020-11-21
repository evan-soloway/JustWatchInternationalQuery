import justwatch
import inspect

from justwatch import JustWatch

def main():

# country code txt
cCodes = open('Alpha2Codes.txt', 'r')

while cCodes:
    

just_watch = JustWatch(
