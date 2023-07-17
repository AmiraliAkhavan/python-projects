# The BMI calculation divides an adult's weight in kilograms (kg) by their height in metres (m) squared.
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

BMI = round(weight / (height ** 2),1)

print("Your current BMI :",BMI )
