

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



