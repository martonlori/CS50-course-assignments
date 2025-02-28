import sys
import csv



def main():

    read_data = []
    write_data = []

    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    else:
        try:
            with open(f"{sys.argv[1]}") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    read_data.append(row)
        except FileNotFoundError:
            sys.exit("First CSV file could not be opened")

        else:
            with open(f"{sys.argv[2]}", "w", newline='') as new_file:
                for i in read_data:
                    last, first = i["name"].strip().split(", ")
                    write_data.append({"first": first, "last": last, "house": i["house"]})

                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for line in write_data:
                    writer.writerow({"first": line["first"] , "last": line["last"], "house": line["house"]})


main()
