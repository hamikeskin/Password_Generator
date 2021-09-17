import random
lower = "hk"
upper = "HK"
numbers = "061"
symbols = "+-"

all = upper+lower+numbers+symbols

length = 8
password = "".join(random.sample(all, length))
print(password)