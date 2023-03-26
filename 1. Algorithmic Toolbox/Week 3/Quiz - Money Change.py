# What does Change(8,  [1, 4, 6]) return?

def change(money):
    numCoins = 0
    while money > 0:
        if money >= 6:
            money = money - 6
        elif money >= 4:
            money = money - 4
        else:
            money = money - 1
        numCoins = numCoins + 1
    return numCoins

print(change(8))