# Use a variable to represent a person's name and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, \t and \n at least once
# Print the name once, so the whitespace is displayed. Then print the name using each of the 3 stripping functions.
name = "  dorian  "
print(f"Names:\n\t{name}\n\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}")