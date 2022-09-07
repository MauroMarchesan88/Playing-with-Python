yuan = int(input("What do you have left in yuan?: "))
yen = int(input("What do you have left in yen?: "))
won = int(input("What do you have left in won?: "))

usd = (yuan * 0.15) + (yen * 0.0074) + (won * 0.00077)

print(usd)
