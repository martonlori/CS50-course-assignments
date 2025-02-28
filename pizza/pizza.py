import sys
from tabulate import tabulate
import csv


data_read = []


def main():

    if len(sys.argv) != 2:
        sys.exit("Wrong number of cmd line arguments")
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Please specify a CSV file")

    else:
        try:
            with open(f"{sys.argv[1]}") as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    data_read.append(row)
        except FileNotFoundError:
            sys.exit("No such file found")

        else:
            print(tabulate(data_read, headers="firstrow",tablefmt="grid"))

main()
