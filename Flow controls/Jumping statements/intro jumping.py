""" 6th october 2026 jumping statements===========
used to alter the flow of the loop 
* Types:
> break : used to stop and exits the loop immeaditely .
> continue : it skips the current iteration moves to next
> pass : null operation >> nothing happens when executing


"""
# break===========
for i in range(1,10):
    if i == 5:
        break
    print(i)
print("ann")
# here only 1, 2 ,3 ,4 only print 5 will be equal and break and go out vof for loop and loop will  be end and to to out of  loop and go to print ann
# if ther is no ann then the prgm is over nothing more


# continue==========
for i in range(1,10):
    if i % 3 == 0: # 1, 2, 3
        continue
    print(i) #1,2,4,5,7,8
# here multiples of 3 will be removed and continue the next one
# so here 1 2 4 5 7 8 will  be printed but 3 6 9 will be not included in the o/p.


for i in range(1,10):
    if i == 3:
        pass
    print(i)
 # nothing happens no  use ALL 1 to 9 will print.
