import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error in CMD line arguments")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        db_reader = csv.DictReader(file)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna_reader = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    for STR in db_reader.fieldnames:
        for row in db_reader:
            result = longest_match(row[STR], dna_reader)
    dict_result = {}
    for STR in db_reader.fieldnames[1:]:
        dict_result[STR] = longest_match(dna_reader, STR)

    # TODO: Check database for matching profiles
    for row in db_reader:
        match = True
        for STR in dict_result:
            if dict_result[STR] != row[STR]:
                match = False
                break
        if match:
            print(row['name'])
            return

def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)
    return longest_run

main()
