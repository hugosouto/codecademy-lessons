# My Solution for Learning Purposes

import random
from datetime import datetime, timedelta

def get_date():
    start_date = datetime(2023, 1, 1)
    end_date   = datetime(2024, 1, 1)

    num_days   = (end_date - start_date).days
    random_day   = random.randint(1, num_days)
    random_date = start_date + timedelta(days=random_day)
    final_date = random_date.strftime(f'%B %d')
    
    return final_date

def my_simulation(num_people):
    print(f"Here's what our room lookes like: \n")
    
    for i in range(0, num_people):
        print(f"Person {i+1}'s birthday: {get_date()}")
    
    prob = round(100*(num_people / 365**(num_people-1)), 2)

    print(f"\nThe probability that two people in a room of {num_people} people have the same birthday is nearly {prob:.0%}")
        
    return

# For testing:
# num_people_in_room = random.randint(2,2)
# simulate(num_people_in_room)


# Codecademy Solution

import random
#Simulate a room with a certain number of people
def simulate(num_people):
  birthdays = []
  print("Here's what our room looks like:\n")
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	#Assign a random birthday to each person
  for i in range(0, num_people):
    #Choose a random month
    month_choice = random.choice(months)
    #Choose a random day based on month
    if month_choice == "February":
      day = random.randint(1, 29)
    elif month_choice == "April" or month_choice == "June" or month_choice == "September" or month_choice == "November":
      day = random.randint(1, 30)
    else:
      day = random.randint(1, 31)
    birthday = month_choice + " " + str(day)
    #Store the birthday
    birthdays.append(birthday)
    print("Person {0}'s birthday: {1}".format(i + 1, birthday))
  calculate_probability(num_people)
  match = False
  #Check for matching birthdays
  for i in range(len(birthdays)):
    if find_duplicates(birthdays, birthdays[i], i):
      match = True
      break
  if not match:
    print("\n\nIn our simulation, no two people have the same birthday")

#Calculate the probability of there being 2 people with the same birthday
def calculate_probability(num_people):
  #Check there is at least 2 people in the room
  if num_people < 2:
    print("\n\nNot enough people in the room!")
    return
  else:
    #Calculate the probability
    numerator = 365
    countdown = 364
    for i in range(2, num_people + 1):
      numerator = numerator * countdown
      countdown -= 1
    denominator = 365 ** num_people
    probability = 1 - numerator/float(denominator)
    #Change probability to percentage
    rounded = round(probability*100, 2)
    print("\n\nThe probability that two people in a room of {0} people have the same birthday is nearly {1}%".format(num_people, rounded))

    
#Find the same birthday within our list of birthdays
def find_duplicates(birthdays_list, birthday, index):
  people = []
  for i in range(len(birthdays_list)):
    if birthdays_list[i] == birthday and i != index:
      people.append(i + 1)
  if people:
    people.append(index + 1)
    print("\n\nIn our simulation, the following people have the same birthdays: ")
    for person in people:
      print("Person {0}".format(person))
    return True
  else:
    return False