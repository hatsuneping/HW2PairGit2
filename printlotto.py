

import random

lotteryNumbers = []
for i in range (0,6):
  number = random.randint(0,9)
  while number in lotteryNumbers:
    number = random.randint(0,9)
  lotteryNumbers.append(number)
lotteryNumbers.sort()
print(">>> Today's lottery numbers are: ") 
print(lotteryNumbers)

r = random.randint(111,999)
s = random.randint(111,999)
t = random.randint(111,999)
u = random.randint(111,999)
print "%03d" % r
print "%03d" % s
print "%03d" % t
print "%03d" % u
