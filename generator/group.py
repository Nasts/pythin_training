# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


# генератор случайных строк
def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # символы в случайно сгенерированной строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
