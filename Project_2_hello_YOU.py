#Ask user for name

name =input("What is your Name? : ")

#Ask user for age
age =input("What is your  age ? : ")


#ask user for city
city = input("What city do you live in ? : ")

#Ask user what they enjoy
love=input("What do you love doing? : ")

#Create output text
string = "Your name is {} and you are {}yrs old and live in {} and you love {}"
output = string.format(name,age,city,love)

#print output screen
print(output)
