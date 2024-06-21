from click import clear
import art
print(art.logo)

auction = {}
bidding_finished = True


def blind_auction():
    name = input("What is your name?: ")
    bid = input("What's your bid? ")
    auction[name] = bid


print("Welcome to the secret auction program")
blind_auction()
ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

while bidding_finished :
    if ans == "yes" :
        clear()
        blind_auction()
        ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ans == "no" :
        max_key = max(auction, key=lambda k: auction[k])
        print(f"The winner is {max_key} with a bid of ${auction[max_key]}")
        bidding_finished = False
                
