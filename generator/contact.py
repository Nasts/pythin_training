# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 1
f = 'data/contacts.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# генератор случайных строк
def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # символы в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [Contact(last_name="", first_name="", address="")] + [
    Contact(last_name=random_string("last_name", 10), first_name=random_string("first_name", 15), address=random_string("address", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
