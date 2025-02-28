from cs50 import get_int

#create 2 half pyramids, promting the user for a positive integer between 1-8
#should repromt if user fails to provide correct number
#there should be 2 spaces between the half pyramids

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for h in range(height, 0, (-1)):
    print(" " * (height - h), end="")
    print("#" * (h + 1), end="")
    print("  ", end="")  # print two spaces
    print("#" * (h + 1))
