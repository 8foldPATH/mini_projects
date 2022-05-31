print("Enter your height in cm:")
height = float(input())
print(height)

print("Enter your weight in kg:")
weight = float(input())
print(weight)

BMI = (weight/(height/100)**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You're in the underweight range.")

elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI}. You're in the healthy range.")

elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}. You're in the overweight range.")

elif 30 <= BMI < 40:
    print(f"Your BMI is {BMI}. You're in the obese range.")