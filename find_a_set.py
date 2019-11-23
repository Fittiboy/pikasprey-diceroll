from random import randint as rint
from datetime import datetime as time

def simulate_dice_rolls(num_rolls, faces, number, min_number_of_rolls):
    print("Rolling dice, please hold...\n")
    start = time.now()
    count = 0
    while True:
        roll_set = [rint(1, faces) for i in range(num_rolls)]
        count += 1
        if roll_set.count(number) >= min_number_of_rolls:
        	break
    end = time.now()
    timediff = end - start
    print("{dice} dices have been rolled! This took {seconds}.{microseconds}s".format(
        dice=count*num_rolls, seconds=timediff.seconds, microseconds=timediff.microseconds))
    return count

def run():
    faces = int(input("\n\n\nHow many faces should the dice have?\n\t"))
    num_rolls = int(input("\nHow many rolls do you need per set?\n\t"))
    number = int(input("\nWhich number are you looking for?\n\t"))
    min_number_of_rolls = int(input("\nHow often should it be in the set at minimum?\n\t"))
    count = simulate_dice_rolls(num_rolls, faces, number, min_number_of_rolls)


    print(f"After simulating {count} sets of rolls, the number",
        f"{number} appeared at least {min_number_of_rolls} times in just a single set.")