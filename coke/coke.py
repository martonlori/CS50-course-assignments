def main():
    print("Running program")
    price = 50
    while price > 0:
        print("Amount Due:", price)
        coin_inserted = int(input("Insert coin: "))
        if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5:
            price -= coin_inserted
        else:
            continue

        if price <=0:
            change_owed = (-1) * price
            print("Change Owed:", change_owed)




main()
