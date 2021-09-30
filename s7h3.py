#ATEFE-JELVE__THURSDAY14-18
#ROUNDOM-NUM-BETWEN-50_100-WHIT-ROUND.ROUND

import random
for i in range(50,100):
    result = random.random()
    x = result * i
    if x < 50 :
        x += 50
print(x)
