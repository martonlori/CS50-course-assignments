# steps:
# 1.Ask user for (valid) input
# 2.Luhn algorithm
# 3.Check the first 2 digits
# 4.Combine these, print results

from cs50 import get_int, get_string
import re

# ccnumber = ""
# while not re.match(r'^\d{13}$|^\d{15}$|^\d{16}$', ccnumber):
# ccnumber = get_string("Number:")
ccnumber = get_string("Number: ")
if len(str(ccnumber)) not in [13, 15, 16]:
    print("INVALID")
    exit()


def multiply_everyotherdigit_addthemtogether(ccnumber):
    i = 1
    sum_of_digits = 0
    cursor = 0
    cclength = len(str(ccnumber))
    while cclength - i - 1 >= 0:
        cursor = int(ccnumber[cclength - i - 1])
        if (2 * cursor) < 10:
            sum_of_digits += (2 * cursor)
        else:
            sum_of_digits += (2 * cursor - 9)
        i += 2
    print(sum_of_digits)
    return sum_of_digits


def sumof_notmultiplied(ccnumber):
    i = 0
    sum_of_digits2 = 0
    cursor = 0
    cclength = len(str(ccnumber))
    while cclength - i > 0:
        cursor = int(ccnumber[cclength - i - 1])
        sum_of_digits2 += cursor
        i += 2
    print(sum_of_digits2)
    return sum_of_digits2


total = (multiply_everyotherdigit_addthemtogether(ccnumber) + sumof_notmultiplied(ccnumber)) % 10
if total == 0:
    if (int(ccnumber[:2]) == 34 or int(ccnumber[:2]) == 37) and len(str(ccnumber)) == 15:
        print("AMEX")
    elif (51 <= int(ccnumber[:2]) <= 55) and len(str(ccnumber)) == 16:
        print("MASTERCARD")
    elif (int(ccnumber[0]) == 4) and (len(str(ccnumber)) == 13 or len(str(ccnumber)) == 16):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
