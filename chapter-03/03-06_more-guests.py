## You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

guests = ['ash ketchum', 'mom', 'charlie']

message = f"Hi {guests[0].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[1].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[2].title()}! Would you like to go to dinner?"
print(message)

print(f"Oh no! It looks like {guests[1].title()} can't make it. What a surprise...")
del guests[1]
guests.append('dad')

message = f"Hi {guests[0].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[1].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[2].title()}! Would you like to go to dinner?"
print(message)

print("Hey guys! I found a biggger table!")
guests.insert(0, 'bill clinton')
guests.insert(1, 'pikachu')
guests.append('jeff gordon')

message = f"Hi {guests[0].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[1].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[2].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[3].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[4].title()}! Would you like to go to dinner?"
print(message)

message = f"Hi {guests[5].title()}! Would you like to go to dinner?"
print(message)