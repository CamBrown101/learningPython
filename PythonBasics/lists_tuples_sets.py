l = ["Bob", "Cam", "Sam"]  # list
t = ("Bob", "Cam", "Sam")  # tuple, cant be changed
s = {"Bob", "Cam", "Sam"}  # set cant have duplicate elements, doesn't keep order


print(t[0])

# access a specific element
l[1] = "Smith"

# Tuples cant be changed
print(l)

# Add to the end of a list
l.append("Greg")
print(l)

# Remove from list
l.remove("Bob")
print(l)

# Add to a set
s.add('smith')
# cant be duplicates
s.add('smith')
print(s)
