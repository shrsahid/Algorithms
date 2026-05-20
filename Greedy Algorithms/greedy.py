def greedy(amount):
    coins= [8,5,4,2,1]

    print("Coins Used: ")

    for coin in coins:
        while amount >= coin:
            amount -= coin

            print (coin,end=" ")

amount= 18

greedy(amount)