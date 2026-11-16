# SESSION 1 — Simple Arithmetic Programs

# 1. BMI Calculator------------
weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in metres: "))

bmi = weight / (height ** 2)

print("BMI is :", bmi)

# 2. Fahrenheit to Celsius
fahrenheit = float(input("Enter temp  in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Celsius:", celsius)


# 3. Kilogram to Pound
kg = float(input("Enter weight in kilograms : "))

pounds = kg * 2.20462

print("Pounds:", pounds)


# 4. Celsius to Fahrenheit
celsius = float(input("Enter temp in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)

# 5. Kilometer to Meter
km = float(input("Enter distance in kilometres: "))

metres = km * 1000

print("Metres:", metres)

# 6. Simple Interest Calculator
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

si = (p * r * t) / 100

print("Simple Interest:", si)

# 7. Area of a Circle
r = float(input("Enter radius: "))

area = 3.14 * (r ** 2) 

print("Area of circle:", area)


# 8. Average of Three Numbers
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

avg = (num1 + num2 + num3) / 3

print("Average:", avg)

# 9. Salary Calculator
basic = float(input("Enter basic salary: "))

hra = basic * 10 / 100
da = basic * 5 / 100
gross = basic + hra + da

print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)

