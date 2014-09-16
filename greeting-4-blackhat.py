# Function
def happy_birthday(name):
    print("Happy Birthday, dear " + name + "!")

# A list of names
names = ["Carol", "Rise", "Trey", "Alain"]

# Calling
for name in names:
    happy_birthday(name)

# A really, really, really long name
print("Test a really, really, really long name")
happy_birthday("Janice Keihanaikukauakahihuliheekahaunaele")

# Something ridiculous
print("Twas brillig, and the slithy toves  Did gyre and gimble in the wabe  All mimsy were the borogoves, And the mome raths outgrabe.")
happy_birthday("Twas brillig, and the slithy toves  Did gyre and gimble in the wabe:  All mimsy were the borogoves,  And the mome raths outgrabe.")

# A number
print(-122.63)
happy_birthday(-122.63)

# A weird type (I choose boolean)
print(True)
happy_birthday(True)

