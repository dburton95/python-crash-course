guests = ['miyamoto', 'shikamaru', 'linus torvald']

print(f"Konichiwa {guests[0].title()}, would you like to have dinner?")
print(f"Hey {guests[1].title()}, come eat.")
print(f"Good afternoon {guests[-1].title()}, you are cordially invited to a dinner party.")

print(f"\nOh no! {guests[-1].title()} can't make it because he is the world's biggest introvert!")

del guests[-1]
guests.append('bill murray')

print(f"\nKonichiwa {guests[0].title()}, would you like to have dinner?")
print(f"Hey {guests[1].title()}, come eat.")
print(f"Good afternoon {guests[-1].title()}, you are cordially invited to a dinner party.")

print("\nHey everyone, we got a bigger table. I'm going to invite a few more guests!")

guests.insert(0, 'eric foreman')
guests.insert(2, 'jack black')
guests.append('father martin')

print(f"\nKonichiwa {guests[0].title()}, would you like to have dinner?")
print(f"Hey {guests[1].title()}, come eat.")
print(f"Good afternoon {guests[2].title()}, you are cordially invited to a dinner party.")
print(f"Good afternoon {guests[3].title()}, you are cordially invited to a dinner party.")
print(f"Good afternoon {guests[4].title()}, you are cordially invited to a dinner party.")
print(f"Good afternoon {guests[-1].title()}, you are cordially invited to a dinner party.")