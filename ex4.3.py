import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def backtrack_steps(number):
    total = []
    for x in range (0,number):
        posn = 0
        steps = 0
        while (posn != 1):
            randint = np.random.random()
            if randint >= 0.5:
                posn += 1
                steps += 1
            else:
                posn -= 1
                steps += 1
        total.append(steps)
    return total


total = backtrack_steps(10000)
f = open('RNAP_steps', 'w')
f.write(str(total))

f.close()
#
# #start at x=0
# #generate a random number
# #if random number < 0.5, assume it goes backwards; else assume it goes forwards
# #new position = x+1 or x-1
# #no_steps += 1
# #if new position > 0 then break.
# add to array
# return array
#
#
