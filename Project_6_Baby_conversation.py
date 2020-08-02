from random import choice

question =["Why are you so hungry?:",
           "How are you so shy ?:",
           "Where are all the dinosours?:"
           ]
question=choice(question)
answer= input(question).strip().lower()

while answer != "just because":
    answer =input("Why?")

print("Oh..Okk")
