import random
import time

dice  = random.randint(1, 6)

def roll_dice():
    print("Rolling the dice...")
    time.sleep(2)
    print("The dice landed on: " + str(dice))
    
if __name__ == "__main__":
    roll_dice()