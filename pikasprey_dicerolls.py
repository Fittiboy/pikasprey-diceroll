from random import randint as rint
from datetime import datetime as time

def simulate_dice_rolls(num_rolls, num_sets, faces):
    print("Rolling dice, please hold...\n")
    start = time.now()
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

def test_small_numbers(num_rolls, num_sets, faces, number, min_number_of_rolls):
    roll_sets = simulate_dice_rolls(num_rolls, num_sets, faces)
    good_sets = check_num_rolls(roll_sets, number, min_number_of_rolls)
    return len(good_sets)

'''This function might be a little slower than simulate_dice_rolls(),
but it gets around the MemoryError issue when too many dice rolls
are simulated to be able to put them into one list of lists

I might remove simulate_dice_rolls() if it turns out to not be
faster'''
def test_large_numbers(num_rolls, num_sets, faces, number, min_number_of_rolls):
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
if num_rolls * num_sets <= 10000:
    count = test_small_numbers(num_rolls, num_sets, faces, number, min_number_of_rolls)
else:
    count = test_large_numbers(num_rolls, num_sets, faces, number, min_number_of_rolls)


print(f"Out of all {num_sets} sets of rolls, {count}",
    f"contained the number {number} at least {min_number_of_rolls} times")