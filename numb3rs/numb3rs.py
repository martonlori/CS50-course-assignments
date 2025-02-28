import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = ip.split(".")
    for seq in numbers:
        if seq.isdigit() == True:
            if int(seq[0]) == 2 and int(seq[1]) == 5:
                pattern = r"^[0-2]{1}[0-5]?[0-5]?\.[0-2]{1}[0-5]?[0-5]?\.[0-2]{1}[0-5]?[0-5]?\.[0-2]{1}[0-5]?[0-5]?$"
            elif int(seq[0]) == 2 and int(seq[1]) != 5:
                pattern = r"^[0-2]{1}[0-5]?[0-9]?\.[0-2]{1}[0-5]?[0-9]?\.[0-2]{1}[0-5]?[0-9]?\.[0-2]{1}[0-5]?[0-9]?$"
            else:
                for i in numbers:
                    if int(i) > 255:
                        return False
                    else:
                        pattern = r"^[0-2]{1}[0-9]?[0-9]?\.[0-2]{1}[0-9]?[0-9]?\.[0-2]{1}[0-9]?[0-9]?\.[0-2]{1}[0-9]?[0-9]?$"

            matches = re.search(pattern, ip)
            if matches:
                return True
            return False

        return False


if __name__ == "__main__":
    main()
