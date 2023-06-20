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

def simulate(num_people):
    print(f"Here's what our room lookes like: \n")
    
    for i in range(0, num_people):
        print(f"Person {i+1}'s birthday: {get_date()}")
    
    prob = round(num_people / 365**(num_people-1), ndigits=10)

    print(f"\nThe probability that two people in a room of {num_people} people have the same birthday is nearly {prob}%")
          
    return

num_people_in_room = random.randint(2,11)

simulate(num_people_in_room)