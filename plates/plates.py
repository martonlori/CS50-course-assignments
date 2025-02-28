def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # min2, max 6 characters altogether
    if not (1 < len(s) < 7):

        return False


    # Must start with min.2 letters
    if not (s[0].isalpha() and s[1].isalpha()):

        return False


    # numbers must be at the end of the plate - first number cannot be 0
    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():

            return False

        elif s[i].isdigit() and s[i+1].isdigit() and s[i] == "0":

            return False

    # no special characters
    for i in s:
        if not i.isalnum():

            return False

    return True


main()
