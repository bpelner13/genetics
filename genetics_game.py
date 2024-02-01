"""This will play the game"""
import sys

import creature


def main():
    """The main function that runs the game"""
    creatures = 0
    if not creatures:
        play = input("Create a creature(y/n)?")
        if play.lower() == 'n':
            print("Ok, enjoy youre day! :)")
            sys.exit()
        name = input("What would you like to name your creature?")
        traits = input("Does your creature have any special traits? (please separate each trait name with a ,)").split(',')
        initial_traits = {}
        for t in traits:
            initial_traits[t] = input(f"Please enter the initial value for trait: {t}")
        mycreature = creature.creature(name, **initial_traits)
        print(mycreature)


if __name__ == "__main__":
    main()
