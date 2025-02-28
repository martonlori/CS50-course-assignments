from datetime import date, timedelta, datetime
import sys
import inflect
import re
import calendar


def main():

    birthday = print(convert(validate(input("Date of Birth: "))))

def validate(birthday):
    try:
        pattern = r"^(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)$"
        matches = re.search(pattern, birthday)
        if matches:
            if 0<= int(matches.group('year')) <= int(datetime.now().year) and 0 < int(matches.group('month')) < 13 and 0 < int(matches.group('day')) <= calendar.monthrange(int(matches.group('year')), int(matches.group('month')))[1]:
                return birthday
            else:
                sys.exit('Invalid date')
        else:
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid format")



def convert(birthday):
    birthday_year, birthday_month, birthday_day = birthday.split('-')
    birthday_date = date(int(birthday_year), int(birthday_month), int(birthday_day))
    difference = (date.today() - birthday_date).days * 24 * 60
    p = inflect.engine()

    return f"{p.number_to_words(difference, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
