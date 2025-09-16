print(r'''__________.__  .__            .___    _____                 __  .__               
\______   \  | |__| ____    __| _/   /  _  \  __ __   _____/  |_|__| ____   ____  
 |    |  _/  | |  |/    \  / __ |   /  /_\  \|  |  \_/ ___\   __\  |/  _ \ /    \ 
 |    |   \  |_|  |   |  \/ /_/ |  /    |    \  |  /\  \___|  | |  (  <_> )   |  \
 |______  /____/__|___|  /\____ |  \____|__  /____/  \___  >__| |__|\____/|___|  /
        \/             \/      \/          \/            \/                    \/ ''')

user_name = input("Enter your name: ").title()
user_bid = float(input("Enter your bid: "))
bidders = {}

def find_highest_bidder():
    highest_bid = 0
    highest_bidder = ""
    for name, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name

    return f"The highest bidder is {highest_bidder} with a bid of {highest_bid}!"


while True:
    bidders[user_name] = user_bid

    new_bidder = input("Would you like to add another bidder? (Y/N): ").upper()
    if new_bidder == "Y":
        print("\n" * 3)
        user_name = input("Enter your name: ").title()
        user_bid = float(input("Enter your bid: "))
    else:
        break

print(find_highest_bidder())