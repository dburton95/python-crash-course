## You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list. ##

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