#sielent auction
#create dictionary
auctions = {}

#logo
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#function that asks name and price
def add_auction():
    name = input("Name: ")
    price = input("Price: ")
    auctions[name] = price
    print("Auction added")
    #clear screen
    print("\n" * 100)

#while loop to keep asking for name and price
while True:
    #logo
    print(logo)
    #ask if user wants to add another auction
    answer = input("Add another auction? (y/n) ")

    if answer == "y":
        add_auction()
    elif answer == "n":
        top_bid = 0
        for i in auctions:
            if int(auctions[i]) > top_bid:
                top_bid = int(auctions[i])
                winner = i
        print("The winner is: " + winner + " with a bid of: " + "$" + str(top_bid))
        break
    else:
        print("Invalid input")
        break


