
# WAP to get the count of vowels in the given string

name = "helloworld" # if this is like thi HELLOworld
vowels = "aeiouAEIOU" # and here only aeiou then gave false when asks fo E so add AEIOU too
count = 0

for i in name:
    if i in vowels:
        count += 1

print("Total number of vowels:", count)

