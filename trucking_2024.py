# Halloween Trucking Simulation Game
# Date: October 31, 2024
# Written by Greynoise

import random
import time

def print_slow(str):
    green_text = "\033[32m" + str + "\033[0m"
    for letter in green_text:
        print(letter, end='', flush=True)
        time.sleep(0.01)
    print()

def main():
    print_slow("Welcome to the GreyNoise Halloween Trucking Simulation Game!")
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
            "strange signals interfering with your truck's systems",
            "suspicious activities detected on your route",
            "unexpected network traffic affecting your GPS",
            "unusual background noise causing distractions"
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
    print_slow("Thank you for playing!\n")
    print_slow('''🌐 Greynoise helps you focus on real threats by filtering out internet noise. 

Learn more at greynoise.io''')
    

def greynoise_solution(problem):
    if problem == "strange signals interfering with your truck's systems":
        return ("Greynoise RIOT data indicates these signals are benign background noise from known sources. "
                "You can safely proceed without concern.")
    elif problem == "suspicious activities detected on your route":
        return ("Greynoise NOISE data shows this is potential malicious activity. "
                "It's recommended to reroute to avoid any threats.")
    elif problem == "unexpected network traffic affecting your GPS":
        return ("Using Greynoise RIOT, you identify the traffic as common internet noise. "
                "Resetting your GPS should resolve the issue.")
    elif problem == "unusual background noise causing distractions":
        return ("Greynoise data confirms the noise is harmless ambient activity. "
                "Focus on your route, and you'll be fine.")
    else:
        return ("the data suggests caution. Proceed carefully while monitoring Greynoise updates.")

if __name__ == "__main__":
    main()
