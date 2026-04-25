def highest_bid(bids):
    max_bid = 0
    max_bidder = ''
    for key, value in bids.items():
        # In case of a tie, the first bidder to reach the highest amount wins
        if value > max_bid:
            max_bid = value
            max_bidder = key
    return max_bidder, max_bid

total_bids = {}

new_bidders = True

while new_bidders:
    name = input('What\'s your name?: ')
    bid = int(input('What\'s your bid?: $'))
    total_bids[name] = bid

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n".lower())
    if continue_bid == "no":
        new_bidders = False
    elif continue_bid == "yes":
        print("\n" * 20)
    else:
        continue_bid = input("Please type 'yes' or 'no'.\n".lower())

winner, max_bid = highest_bid(total_bids)
print(f'The winner is {winner} with a bid of ${max_bid}')