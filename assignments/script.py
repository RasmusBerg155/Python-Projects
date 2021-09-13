# This is a comment

# This will print out the list alphabetically sorted
l = ['Ib', 'iben', 'Claus', 'Torben']

print(sorted(l))

# This will print out the list alphabetically sorted from the last letter in each name.
def last_letter(x):
    return x[-1]

last_letter('Claus')

print(sorted(l, key=last_letter))

