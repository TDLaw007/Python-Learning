# Write a program that prompts the user to enter their score (out of 100).
# Displays their corresponding grade based on the following criteria:

# Scores 90 and above: Grade A
# Scores 80 to 89    : Grade B
# Scores 70 to 79    : Grade C
# Scores 60 to 69    : Grade D
# Scores below 60    : Grade F

score = input("What is your score? ")
age = input ("How old are you? ")
score = int(score)
age = int(age)
grade = score
grade = str

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = ("B")
elif score >= 70:
    grade = ("C")
elif score >= 60:
    grade = ("D")
else:
    grade = ("F")


if age <= 11:
    print(f"Great job! you've got an {grade}+")
else:
    print(f"Good job! you've got an {grade}")