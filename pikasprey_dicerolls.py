from random import randint as rint
from datetime import datetime as time

def simulate_dice_rolls(num_rolls, num_sets, faces):
    start = time.now()
    print("Rolling dice, please hold...\n")
    roll_sets = [[rint(1, faces) for i in range(num_rolls)] for i in range(num_sets)]
    end = time.now()
    timediff = end - start
    print("All {num_sets} sets are rolled! This took {seconds}.{microseconds}s".format(
        num_sets=num_sets, seconds=timediff.seconds, microseconds=timediff.microseconds))
    return roll_sets


def check_num_rolls(roll_sets, number, min_number_of_rolls):
    good_sets = []
    for roll_set in roll_sets:
        if roll_set.count(number) >= min_number_of_rolls:
            good_sets.append(roll_set)
    return good_sets

faces = int(input("\n\n\nHow many faces should the dice have? "))
num_rolls = int(input("\nHow many rolls do you need per set? "))
num_sets = int(input("\nHow many sets of rolls would you like to simulate? "))
roll_sets = simulate_dice_rolls(num_rolls, num_sets, faces)
number = int(input("\nWhich number are you looking for? "))
min_number_of_rolls = int(input("\nHow often should it be in the sets at minimum? "))
good_sets = check_num_rolls(roll_sets, number, min_number_of_rolls)
print(f"Out of all {num_sets} sets of rolls, {len(good_sets)} contained the number {number} at least {min_number_of_rolls} times")
