import random

chars = "abcdefghijkmnopqrstuvwxyz"
CHARS = chars.upper()
symbols = "[]{}()*;_-=/,0!@#$"
numbers = "0123456789"

allVariables  = chars + CHARS + symbols + numbers

len = 16

password = "".join(random.sample(allVariables,len))

print(password)