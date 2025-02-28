import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # start, finish = s.split(" to ", maxsplit=1)
    # if int(start[0]) > 12:
    #     raise ValueError
    # else:
    #     if "AM" in start:
    #         start_pattern = r"^([1-9][0-2]?)(?::([0-6]?[0-9]?))? AM$"
    #         start_matches = re.search(start_pattern, start)
    #         if start_matches:
    #             start_hour = int(start_matches.group(1))
    #             if 0 <= int(start_matches.group(2)) < 61:
    #                 start_minutes = int(start_matches.group(2))
    #             else:
    #                 raise ValueError

    #     elif "PM" in start:
    #         start_pattern = r"^([1-9][0-2]?)(?::([0-6]?[0-9]?))? PM$"
    #         start_matches = re.search(start_pattern, start)
    #         if start_matches:
    #             start_hour = int(start_matches.group(1)) + 12
    #             if 0 <= int(start_matches.group(2)) < 61:
    #                 start_minutes = int(start_matches.group(2))
    #             else:
    #                 raise ValueError

    # if int(finish[0]) > 12:
    #     raise ValueError
    # else:
    #     if "AM" in finish:
    #         finish_pattern = r"^([1-9][0-2]?)(?::([0-6]?[0-9]?))? AM$"
    #         finish_matches = re.search(finish_pattern, finish)
    #         if finish_matches:
    #             finish_hour = int(finish_matches.group(1))
    #             if 0 <= int(finish_matches.group(2)) < 61:
    #                 finish_minutes = int(finish_matches.group(2))
    #             else:
    #                 raise ValueError

    #     elif "PM" in finish:
    #         finish_pattern = r"^([1-9][0-2]?)(?::([0-6]?[0-9]?))? PM$"
    #         finish_matches = re.search(finish_pattern, finish)
    #         if finish_matches:
    #             finish_hour = int(finish_matches.group(1)) + 12
    #             if 0 <= int(finish_matches.group(2)) < 61:
    #                 finish_minutes = int(finish_matches.group(2))
    #             else:
    #                 raise ValueError

    # return f"{start_hour:02}:{start_minutes:02} to {finish_hour:02}:{}"


    pattern = r"^(?P<start_hour>[1-9][0-2]?)(?::(?P<start_minutes>[0-6][0-9]))? (?P<am_or_pm_start>AM|PM) to (?P<finish_hour>[1-9][0-2]?)(?::(?P<finish_minutes>[0-6][0-9]))? (?P<am_or_pm_finish>AM|PM)$"
    matches = re.search(pattern,s)
    if matches:
        if int(matches.group('start_hour')) > 12:
            raise ValueError
        else:
            if matches.group('start_minutes'):
                if  0<= int(matches.group('start_minutes')) < 60:
                    if matches.group('am_or_pm_start') == "AM":
                        start_hour = int(matches.group('start_hour'))
                        start_minutes = int(matches.group('start_minutes'))
                        if start_hour == 12:
                            start_hour = 0
                    elif matches.group('am_or_pm_start') == "PM" and int(matches.group('start_hour')) != 12:
                        start_hour = int(matches.group('start_hour')) + 12
                        start_minutes = int(matches.group('start_minutes'))

                    else:
                        start_minutes = 0
                        start_hour = 12
                else:
                    raise ValueError
            else:
                if matches.group('am_or_pm_start') == "AM":
                        start_hour = int(matches.group('start_hour'))
                        start_minutes = 0
                        if start_hour == 12:
                            start_hour = 0
                elif matches.group('am_or_pm_start') == "PM" and int(matches.group('start_hour')) != 12:
                    start_hour = int(matches.group('start_hour')) + 12
                    start_minutes = 0

                else:
                    start_hour = 12
                    start_minutes = 0

        if int(matches.group('finish_hour')) > 12:
            raise ValueError
        else:
            if matches.group('finish_minutes'):
                if  0<= int(matches.group('finish_minutes')) < 60:
                    if matches.group('am_or_pm_finish') == "AM":
                        finish_hour = int(matches.group('finish_hour'))
                        finish_minutes = int(matches.group('finish_minutes'))
                        if finish_hour == 12:
                            finish_hour = 0
                    elif matches.group('am_or_pm_finish') == "PM" and int(matches.group('finish_hour')) != 12:
                        finish_hour = int(matches.group('finish_hour')) + 12
                        finish_minutes = int(matches.group('finish_minutes'))

                    else:
                        finish_hour = 12
                        finish_minutes = 0
                else:
                    raise ValueError
            else:
                if matches.group('am_or_pm_finish') == "AM":
                        finish_hour = int(matches.group('finish_hour'))
                        finish_minutes = 0
                        if finish_hour == 12:
                            finish_hour = 0
                elif matches.group('am_or_pm_finish') == "PM" and int(matches.group('finish_hour')) != 12:
                    finish_hour = int(matches.group('finish_hour')) + 12
                    finish_minutes = 0

                else:
                    finish_hour = 12
                    finish_minutes = 0
    else:
        raise ValueError

    return f"{start_hour:02}:{start_minutes:02} to {finish_hour:02}:{finish_minutes:02}"




if __name__ == "__main__":
    main()
