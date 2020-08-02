films={
    "3 Idiots":[3,5],
    "Zombie":[18,5],
    "Ms Dhoni":[3,5],
    "Ghost Burster":[12,5],
    "Avengers":[16,5],
   }
while True:
    choice=input("Which film would you want to see").rstrip().title()

    if choice in films:
        age=int(input("How old you are").strip())

         #check user mage
        
        if age>=films[choice][0]: 

          #check Tickets
            if films[choice][1]>0:
                  print("Here are your tickets , Enjoy the movie!")
                  films[choice][1]=films[choice][1]-1
            else:
                print("Sorry,we are sold out")
            
                
                   
        else:
            print("You are too young to see")
 
    else:
        print("We dont have this film")
    
