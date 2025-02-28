import sys
from PIL import Image, ImageOps
import os


def main():



    if len(sys.argv) != 3:
        sys.exit("Incorrect number of command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"] or os.path.splitext(sys.argv[2])[1].lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Input or output is not the correct file format")
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        sys.exit("Output file format does not match the input file format")
    else:

        try:
            # with Image.open(f"{sys.argv[1]}") as image:
            #     size = image.size
            #     fitted_image = ImageOps.fit(image, size)

            with Image.open("shirt.png") as shirt:
                size = shirt.size
                fitted_shirt = ImageOps.fit(shirt, size)
                with Image.open(f"{sys.argv[1]}") as image:
                    fitted_image = ImageOps.fit(image, size)
                    fitted_image.paste(fitted_shirt, (0, 0), fitted_shirt)
                fitted_image.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("Input file not found")


main()
