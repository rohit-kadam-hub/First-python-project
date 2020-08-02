known_users=["Alice","Bob","Clair","Dan","Emma","Fred","George","Harry"]


while True:
   print("Hey,Hi! My name is Rohit,")
   name=input("What is your name").strip().capitalize()
   if name in known_users:
       print("Ooh, Hello {}".format(name))
       remove=input("Would you like to delete your name from system(y/n): ").lower()
       
       if remove =="y":
          
           known_users.remove(name)
           print(known_users)
       elif remove=="n":
            print("No problem,You can stay")
           
           
   else:
       print("Hmm I don't think i have met you yet {}".format(name))
       add= input("Would you like to be in our system(y/n):").strip().lower()
       if add =="y":
           known_users.append(name)
           print(known_users)
       elif add=="n":
            print("No problem, See you")
