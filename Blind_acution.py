from click import clear
import art
print(art.logo)
acution = {}

print("Welcome to the secret auction program")

def blind_acution():
    name = input("What is your name?: ")
    bid = input("What's your bid? ")
    acution[name] = bid

blind_acution()
ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
x = True
while x :
    if ans == "yes" :
        clear()
        blind_acution()
        ans = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if ans == "no" :
        max_key = max(acution, key=lambda k: acution[k])
        print(f"The winner is {max_key} with a bid of ${acution[max_key]}")
        x = False
