import random
import string

def randomString(stringLength):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))

for x in range(100):
    print(randomString(20))
