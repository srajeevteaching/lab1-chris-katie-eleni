# Programmers: Katie, Chris, Eleni
# Course: CS151, Dr. Rajeev
# Date: September 16, 2021
# Lab 1

# Creating mL input string
mlInput = input("Enter the number of milliliters(mL) here.  ")
# typecast input value --> is now an integer
mlInt = int(mlInput)
# creation of tsp and tbsp conversion variables
tsp = mlInt / 5
tbsp = tsp / 3
# print statements
print("The equivalent number of teaspoons is: ", tsp, "teaspoons.")
print("The equivalent number of tablespoons is: ", tbsp, "tablespoons.")