rooms = ['bedroom', 'dressing room', 'living room', 'office', 'bathroom']

print(f"My house has {len(rooms)} rooms.")
print(f"These are the rooms:\n{rooms[0]}\n{rooms[1]}\n{rooms[2]}\n{rooms[3]}\n{rooms[4]}")

print(f"\nLet's reverse the order.")
rooms.reverse()
print(f'{rooms}\nNice!')

print(f"\nThese are the rooms in alphabetical order: \n{sorted(rooms)}")
print(f"These are the rooms in reverse alphabetical order: \n{sorted(rooms, reverse=True)}")

print("\nLet's add a room.")
rooms.append('secret room')
print(rooms)
print(f"Just Kidding! There's no {rooms[-1]}! Let's get rid of it... But I might want to talk about it again..")

popped_room=rooms.pop()
print(rooms)
print(f"That's better. What was that room we made up called again? Oh yeah! It was {popped_room}! :D")
print("Let's add it back one more time.")
rooms.append(popped_room)
print(f"\n{rooms}\nNice!\nOk we'll delete it for good this time")
del rooms[-1]

print(f"\n{rooms}\nOk it's gone for good now.\n\nHow about some permanent sorting?")
rooms.sort()
print(f"{rooms}\n\n Reverse reverse!")
rooms.sort(reverse=True)
print(f"\n\n{rooms}\nCha cha real smooth.")