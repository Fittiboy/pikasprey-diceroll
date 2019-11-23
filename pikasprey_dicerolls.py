from random import randint as rint
from datetime import datetime as time

def simulate_dice_rolls(num_rolls, num_sets, faces, number, min_number_of_rolls):
    print("Rolling dice, please hold...\n")
    start = time.now()
    count = 0
    for i in range(num_sets):
        roll_set = [rint(1, faces) for i in range(num_rolls)]
        if roll_set.count(number) >= min_number_of_rolls:
            count += 1
    end = time.now()
    timediff = end - start
    print("All {num_sets} sets are rolled! This took {seconds}.{microseconds}s".format(
        num_sets=num_sets, seconds=timediff.seconds, microseconds=timediff.microseconds))
    return count

faces = int(input("\n\n\nHow many faces should the dice have? "))
num_rolls = int(input("\nHow many rolls do you need per set? "))
num_sets = int(input("\nHow many sets of rolls would you like to simulate? "))
number = int(input("\nWhich number are you looking for? "))
min_number_of_rolls = int(input("\nHow often should it be in the sets at minimum? "))
count = simulate_dice_rolls(num_rolls, num_sets, faces, number, min_number_of_rolls)


print(f"Out of all {num_sets} sets of rolls, {count}",
    f"contained the number {number} at least {min_number_of_rolls} times")