
import numpy as np
from random import uniform
from random import random
import sys
import json
import io
import codecs
import re
from functools import partial

f = io.open('data/message_1.json', mode="r", encoding="latin-1")

fix_mojibake_escapes = partial(
     re.compile(rb'\\u00([\da-f]{2})').sub,
     lambda m: bytes.fromhex(m.group(1).decode()))

with open('data/message_1.json', 'rb') as binary_data:
    repaired = fix_mojibake_escapes(binary_data.read())

data = json.loads(repaired.decode('utf8'))
messages = data["messages"]

with codecs.open("data/chatTrainData.txt", "w", "utf-8-sig") as writeFile:
    for i in range(len(messages)):
        try:
            writeFile.write(messages[i]["content"] + '\r\n')
        except KeyError:
            continue