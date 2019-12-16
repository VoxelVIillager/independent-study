"""This is a random word generator made to act like a rock paper scissors game."""


# define lists we will need and random number generator
import random
comp_throw = str()
person_throw = str()
rand_num = random.randint(1, 3)

# determines comp_throw
if rand_num == int(1):
    comp_throw = str("rock")
if rand_num == int(2):
    comp_throw = str("paper")
if rand_num == int(3):
    comp_throw = str("scissors")

#determines person_throw
person_throw = str(raw_input("rock, paper, scissors, shoot!"))

# insert code here to reroute play if person_throw is the same as comp_throw

# if person throws rock
if person_throw == str("rock"):
    if comp_throw == str("paper"):
        print ("paper beats rock")
    else:
        print ("rock beats scissors")

    # if person throws scissors - make this look like the code above
    if person_throw == str("scissors"):
        if comp_throw == str("paper"):
            print ("scissors beats paper")
        if person_throw == str("scissors"):
            if comp_throw == str("rock"):
                print ("rock beats scissors")

            # if person throws paper
            if person_throw == str("paper"):
                if comp_throw == str("rock"):
                    print ("paper beats rock")
                if person_throw == str("paper"):
                    if comp_throw == str("scissors"):
                        print ("scissors beats paper")

# person_throw is player's input
# compare person_throw to comp_throw
