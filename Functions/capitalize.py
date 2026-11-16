# o capitalize the 1st and 4th letters of "python"

name = "python"

name = name[0].upper() + name[1:3] + name[3].upper() + name[4:]

print(name)

# Remember:
# - Python indexing starts from 0.
# - upper() converts a letter into uppercase.
# - String slicing helps combine the required characters.