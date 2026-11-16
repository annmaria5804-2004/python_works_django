# wap to return the most occuring char from the string given using function

def most_occuring(s):
    max_count = 0
    max_char = ""

    for i in s:
        count = s.count(i)
        if count > max_count:
            max_count = count
            max_char = i

    print("Most occurring character:", max_char)

s = input("Enter a string: ")
most_occuring(s)
