import random
max_num = 3


def shuffle(current_shuffle, remaining_shuffle):
    if len(current_shuffle) == max_num:
        for item in current_shuffle:
            print(item, end=' ')
        print()
    else:
        for i in range(0, 10):
            new_order = current_shuffle.copy() # Make a copy.
            new_order.append(remaining_shuffle[str(len(current_shuffle) + 1)][i])
            shuffle(new_order, remaining_shuffle)

def random_shuffle(categories):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)

    print("{} {} {}".format(categories['1'][num1], categories['2'][num2], categories['3'][num3]))

def main():
    categories = {
        '1' : ["Sorry I can't come", "Please forgive my absense,", "This is going to sound crazy but", "Get this:", "I can't go because", "I know you're going to hate me but", 
               "I was minding my own business and boom!", "I feel terrible but", "I regretfully cannot attend,", "This is going to sound like an excuse but"],
        '2' : ["my nephew", "the ghost of Hitler", "the Pope", "my ex", "a high school marching band", "Dan Rather", "a sad clown", "the kid from Air Bud", 
               "a professional cricket team", "my Tinder date"],
        '3' : ["just shit the bed", "died in front of me", "won't stop telling knock knock jokes", "is having a nervous breakdown", "gave me syphilis", 
              "poured lemonade into my gas tank", "stabbed me", "found my box of human teeth", "stole my bicycle", "posted my nudes on Instagram"]
        }
    
    print("Choose whether you wish to have all shuffled options, or one randomly chosen.\n"
          "a - all shuffled options\n"
          "b - one randomly chosen.\n"
          "q - Quit the program.")
    option = input()
    while option != 'q':
        if option == 'a':
            shuffled = []
            shuffle(shuffled, categories)
            option = input("Please choose another input: ")
        elif option == 'b':
            random_shuffle(categories)
            option = input("Please choose another input: ")
        else:
            print("Please choose from one of the options. {} is not a valid option.".format(option))
            option = input("Please choose another input: ")
        
if __name__ == '__main__':
    main()
