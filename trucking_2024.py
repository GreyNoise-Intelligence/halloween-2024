# Halloween Trucking Simulation Game with Green Font

import random
import time

def print_slow(str):
    green_text = "\033[32m" + str + "\033[0m"
    for letter in green_text:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()

def main():
    print_slow("Welcome to the Halloween Trucking Simulation Game!")
    print_slow("You are a truck driver tasked with delivering Halloween candies to various towns.")
    print_slow("However, spooky obstacles await you on the road...")
    name = input("\033[32mFirst, what's your name, driver? \033[0m")
    print_slow(f"Alright, {name}, let's begin your journey!\n")

    deliveries = ["Spooky Hollow", "Ghost Town", "Pumpkinville", "Witch's Creek"]
    random.shuffle(deliveries)
    success = 0

    for town in deliveries:
        print_slow(f"Your next delivery is to {town}.")
        print_slow("But wait, there's a problem ahead!")

        problem = random.choice([
            "a haunted bridge",
            "a roadblock by mischievous spirits",
            "a cyber-attack on your GPS",
            "an eerie fog causing low visibility"
        ])
        print_slow(f"You encounter {problem}.")

        print_slow("To find a solution, you decide to consult Greynoise data.")
        print_slow("Analyzing data...")
        time.sleep(2)
        solution = greynoise_solution(problem)

        print_slow(f"According to Greynoise data, {solution}")

        choice = input("\033[32mDo you follow the Greynoise recommendation? (yes/no) \033[0m").lower()
        if choice == 'yes':
            print_slow("You follow the advice and continue your journey.")
            success += 1
        else:
            print_slow("You ignore the advice and get lost in the night.")
            print_slow("You miss the delivery.")
        print_slow("\n")

    print_slow(f"Your deliveries completed: {success}/{len(deliveries)}")
    if success == len(deliveries):
        print_slow("Congratulations! You successfully delivered all the candies. The children are happy!")
    else:
        print_slow("Some deliveries were missed. The children are disappointed, but you did your best.")
    print_slow("Thank you for playing!")

def greynoise_solution(problem):
    if problem == "a haunted bridge":
        return "the bridge is an illusion. Proceed with caution and you'll pass through safely."
    elif problem == "a roadblock by mischievous spirits":
        return "the spirits are attracted to light. Use your headlights to distract them and clear the path."
    elif problem == "a cyber-attack on your GPS":
        return "resetting your GPS and using a physical map will help you navigate around the cyber interference."
    elif problem == "an eerie fog causing low visibility":
        return "taking a detour through the Whispering Woods, as per the data, will bypass the fog."
    else:
        return "the data suggests to wait until dawn, but time is of the essence!"

if __name__ == "__main__":
    main()
