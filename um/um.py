import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    matches = re.findall(pattern, s.lower())
    return matches.count("um")


if __name__ == "__main__":
    main()
