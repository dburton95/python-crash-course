## You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

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

print("Oh No! Looks like we can't get the table after all. I'm only bringing two people.")

angry_guest = guests.pop(0)
print(f"Sorry {angry_guest.title()}. I guess you have to go home.")

angry_guest = guests.pop(0)
print(f"Sorry {angry_guest.title()}. I guess you have to go home.")

angry_guest = guests.pop(0)
print(f"Sorry {angry_guest.title()}. I guess you have to go home.")

angry_guest = guests.pop(0)
print(f"Sorry {angry_guest.title()}. I guess you have to go home.")

print(f"Don't worry {guests[0].title()}, you're still invited.")
print(f"Don't worry {guests[1].title()}, you're still invited.")

del guests[0]
del guests[0]
print(guests)