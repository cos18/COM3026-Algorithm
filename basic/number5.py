import random
import time

startTime = time.time()

randlist = [random.randint(1, 1000000) for i in range(500)]
randlist.sort(reverse=True)
print(randlist[4])

endTime = time.time() - startTime
print('\nTime : ', endTime)