#  write a program that asks the user to enter a person's age
#  the program should then display a message indicating
#  whether the person is an infant, child, teenager, or adult

print("Hi!\nWelcome to the Age Classifier program.\n")
age = int(input("Please enter a person's age: \n"))

#  [if the person is 1 year old or less,
#  they are an infant]
if age <= 1:
    print("The person's age you have entered classifies them as an infant.")

#  [if the person is older than 1 year
#  but younger than 13, they are a child]
elif age > 1 and age < 13:
    print("The person's age you have entered classifies them as a child.")

#  [if the person is at least 13 years old
#  but less than 20 they are a teenager]
elif age >= 13 and age < 20:
    print("The person's age you have entered classifies them as a teenager.")

#  [if the person is at least 20 years old
#  they are an adult]
else:
    print("The person's age you have entered classifies them as an adult.")
