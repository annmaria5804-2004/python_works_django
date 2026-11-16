# get the strong number in range 1 to 500

for number in range(1, 501):

    total = 0

    for num in str(number):

        fact = 1

        for j in range(1, int(num) + 1):
            fact *= j

        total += fact

    if total == number:
        print(f"{number} is a strong number")
        
        
# get the strong number in range 10 to 500

for number in range(10, 501):

    total = 0

    for num in str(number):

        fact = 1

        for j in range(1, int(num) + 1):
            fact *= j

        total += fact

    if total == number:
        print(f"{number} is a strong number")