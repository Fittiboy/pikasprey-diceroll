import find_a_set
import pikasprey_dicerolls

while True:

    choice = int(input("Which method would you like to use?\n\t1. Fixed number of sets\n\t2. Simulate until set found\n\t\t"))

    if choice == 1:
        pikasprey_dicerolls.run()
    elif choice == 2:
        find_a_set.run()
    else:
        print("\nPlease enter either 1 or 2!\n\n")

    again = ""
    while again not in ["y", "n"]:
        again = input("Do you want to try again? (Enter either y for yes or n for no)\n\t").lower()
    
    if again == "n":
        print("\n\n\t\tHave a nice day!!")
        break
