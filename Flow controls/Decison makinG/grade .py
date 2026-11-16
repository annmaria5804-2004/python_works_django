# ask the student to enter the mark
# if mark from 91-100(inclusive) print grade a
# if mark from 81-90 print grade b
# if mark from 71-80 print grade c
# if mark from 61-70 print grade d
# if mark 60 0r below failed

mark = int(input("enter the mark: "))
if mark >=91 and mark <=100:
    print("your grade is A")
elif mark >=81 and mark <=90:
    print("your grade is B")
elif mark >=71 and mark <=80:
    print("your grade is C")
elif mark >=61 and mark <=70:
    print("your grade is D")
elif mark <= 60:
    print("you are failed")
else:
    print("invalid")