import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error in CMD line arguments")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        db_reader = csv.DictReader(file)
        fieldnames = db_reader.fieldnames
        rows = list(db_reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna_reader = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    dict_result = {}
    for STR in fieldnames[1:]:
        dict_result[STR] = longest_match(dna_reader, STR)

    # TODO: Check database for matching profiles
    for row in rows:
        match = True
        for STR in dict_result:
            if dict_result[STR] != int(row[STR]):
                match = False
                break
        if match:
            print(row['name'])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
