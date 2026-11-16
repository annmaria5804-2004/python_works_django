# create a class
# method1 : accept a string and return the count of each char  in the string
# method2 : accept a num and check the num is prime or Not
#  method3 : accept a list of numbers and return the sum of even numbers from the list

class My:

    # Method 1: Count each character in a string
    def char_count(self, s):
        for i in s:
            print(i, ":", s.count(i)) # count() counts how many times each character occurs.

    # Method 2: Check whether a number is prime or not
    def prime(self, num):
        if num <= 1:
            print("Not a Prime Number")
        else:
            for i in range(2, num):
                if num % i == 0:
                    print("Not a Prime Number")
                    break
            else:
                print("Prime Number")

    # Method 3: Sum of even numbers in a list
    def even_sum(self, lst):
        total = 0
        for i in lst:
            if i % 2 == 0:
                total += i

        return total


# Creating an object
obj1 = My()

# Method 1
s = input("Enter a string: ")
obj1.char_count(s)

# Method 2
num = int(input("Enter a number: "))
obj1.prime(num)

# Method 3
lst = [10, 15, 20, 25, 30]
print("Sum of even numbers:", obj1.even_sum(lst))