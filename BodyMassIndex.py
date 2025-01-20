weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height**2)
                                                              # Question 3
if bmi < 18.5:
    weight_status = "Underweight"
elif bmi < 24.9:
    weight_status = "Normal"
elif bmi < 29.9:
    weight_status = "Overweight"
else:
    weight_status = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the '{weight_status}' range")