# Write a function to convert a name into initials. This kata strictly takes two
# ords with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris = > S.H

# Patrick Feeney = > P.F

def abbrev_name(name):
    split_list = name.split()
    return f"{split_list[0][0]}.{split_list[1][0]}".upper()


print(abbrev_name("Cam brown"))
