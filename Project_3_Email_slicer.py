#get user email addr

email=input("Enter Email:").strip()

#slice out user name
user = email[:email.index("@")]

#slice domain name
             
domain = email[email.index("@")+1:]

#format message
             
output = "Your username is {} and Your domain is {}".format(user,domain)

#Print             

print(output)             
