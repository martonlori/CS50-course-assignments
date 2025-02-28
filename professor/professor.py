import random


def main():
    level = get_level()
    wrongs = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        counter = 0

        while True:
            answer = int(input(f"{x} + {y} = "))
            if answer != (x + y):
                print("EEE")
                counter +=1
                if counter == 3:
                    print(f"{x} + {y} = {x + y}")
                    wrongs +=1
                    break
                else:
                    continue
            else:
                break

    print(f"Score: {10-wrongs}")





def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            print("Enter 1, 2 or 3")
            continue
        else:
            if not (n==1 or n==2 or n==3):
                print("Enter 1, 2 or 3")
                continue
            else:
                return n


def generate_integer(level):
    if level == 1:
        n = random.randint(0,9)
        return n
    elif level == 2:
        n = random.randint(10,99)
        return n
    elif level == 3:
        n = random.randint(100,999)
        return n
    else:
        raise ValueError



if __name__ == "__main__":
    main()
