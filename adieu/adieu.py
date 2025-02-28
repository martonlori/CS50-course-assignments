import inflect
import sys


def main():
    names=[]
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ")
            if name:
                names.append(name)

        except EOFError:
            print("")
            break


    print(f"Adieu, adieu, to {p.join(names)}")

main()
