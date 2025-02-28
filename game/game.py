import random
import sys

def main():

    while True:
        try:
            n = int(input("Level: "))

        except ValueError:
            print("Enter a positive integer")
            continue

        else:
            if n < 1:
                print("Enter a positive integer")
                continue
            else:
                level = random.randint(1, n)
                while True:
                    try:
                        guess = int(input("Guess: "))
                    except ValueError:
                        print("Enter a positive integer")
                        continue
                    else:
                        if guess < 1:
                            print("Enter a positive integer")
                            continue
                        else:
                                if level > guess:
                                    print("Too small!")
                                elif level < guess:
                                    print("Too large!")
                                elif level == guess:
                                    print("Just right!")
                                    sys.exit()

main()
