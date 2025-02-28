def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        try:
            date = input("Date: ").strip(" ")
            if "/" in date:
                    m,d,y = date.split("/")
                    if any(char.isalpha() for char in m):
                          continue
            elif ", " in date:
                    m,d = date.split(", ")[0].split(" ")
                    y = date.split(", ")[1]
                    if any(char.isdigit() for char in m):
                          continue

            else:
                  print("Invalid format")
                  continue

            if m not in months:
                try:
                    if not (0 < int(m) < 13):
                            print("Invalid date")
                            continue
                except ValueError:
                      print("Invalid month name")
                      continue

                else:
                      m = int(m)
            else:
                  m = months.index(m) + 1


            if not 0 < int(d) < 32:
                  print("Invalid day")
                  continue
            elif not 0 < int(y) < 10000:
                  print("Invalid year")
                  continue
        except:
              print("Got here")
              continue
        else:
              date_output = "-".join([y,str(m).zfill(2),str(d).zfill(2)])
              print(date_output)
              break
















main()
