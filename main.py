import os
from builtins import enumerate

from modules.binarysearch import *
import json
import names

savefile = open("data.json")
people = json.loads(savefile.read())
#people = ["Zane Miller"]

res = enchancedbinarysearch(array=people, element="Paul A")
print(res)

