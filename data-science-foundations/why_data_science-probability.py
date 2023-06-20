import random
from simulate import simulate, my_simulation

 #Change this number (keep it smaller than 100 to save processing power)
num_people_in_room = random.randint(2,100)

my_simulation(num_people_in_room)
simulate(num_people_in_room)

# The output should look like this:
# 
# '''
# Here's what our room looks like:
# 
# Person 1's birthday: November 27
# Person 2's birthday: July 28
# 
# The probability that two people in a room of 2 people have the same birthday is nearly 0.27%
# 
# In our simulation, no two people have the same birthday
# '''