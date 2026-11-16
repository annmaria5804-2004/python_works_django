#23/09/2026 wednesday---------------
# grt the total no of days from user and convert the days into hrs and then convert the hrs to mun and finally convert mints into seconds.
#-----------------------------------------------------
# ndays *24 and hrs *60 and min *60 and *sec
#----------------------------------------

# If the question gives days
days = int(input("Enter the number of days: "))

hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

# If the question gives Hours
hours = int(input("Enter number of hours: "))

days = hours / 24
minutes = hours * 60
seconds = minutes * 60

print("Days:", days)
print("Minutes:", minutes)
print("Seconds:", seconds)


# If the question gives Minutes
minutes = int(input("Enter number of minutes: "))

hours = minutes / 60
days = hours / 24
seconds = minutes * 60

print("Days:", days)
print("Hours:", hours)
print("Seconds:", seconds)

# If the question gives Seconds
seconds = int(input("Enter number of seconds: "))

minutes = seconds / 60
hours = minutes / 60
days = hours / 24

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)



# Easy conversion rule to remember
#---------------------------------------
# Going to a smaller unit → multiply =

#Days → Hours: × 24
#Hours → Minutes: × 60
#Minutes → Seconds: × 60

#Going to a larger unit → divide =

#Seconds → Minutes: ÷ 60
#Minutes → Hours: ÷ 60
#Hours → Days: ÷ 24