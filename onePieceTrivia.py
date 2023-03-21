print("Welcome to One Piece Trivia!")

# positive = ["Yes", "yes", "Yup", "yup", "yah", "yeah", "yea", "sure"]
# negative = ["No", "no", "Nope", "nope", "nah", "Nah"]

while True:
  greeting = input("Hello contestant! Ready to play? ")
  greeting = greeting.lower()
  if greeting == "yes" or greeting == "yeah" or greeting == "yup" or greeting == "yah" or greeting == "sure":
    print("\nAwesome! Let us get started then.")
    break
  elif greeting == "no" or greeting =="nope" or greeting == "nah":
    print("\nOk, the program will now shut off.")
    print("\n")
    quit("Participant did no want to play the game.")
  else:
    print("\nYou have made an error. If you would like to continue, ")
    print(f"please select the following: yes, yeah, yup, yah, or sure")
    print(f"If you do not wish to continue, responde with: no, nope, or nah")
    continue
# Using the funcition quit(), the program will exit if there is any input besides "Yes" or "yes".

name = input("\nSo, to start off, what is your name? ")
print(f"Nice to meet you {name}!")
print("\nNow, let us get started with our first question")

# I am nesting a list within a list, within a list. This makes it so I will only have to call my defined function one time.
triviaList = [
['\nWho ate the "Chop-Chop" devil fruit?', ["A. Bon Clay", "B. Buggy the Clown", "C. Daz Bones", "D. Clawador"], "b", "Buggy the Clown"],
["\nWho was the 3rd person to become member of the Straw Hat Pirates?", ["A. Sanji", "B. Nami", "C. Ussop", "D. Zoro"], "b", "Nami"],
["\nWhat is White Beard's full name?", ["A. Edward Newgate", "B. Marshal D. Teach", "C. Basil Hawkins", "D. Demoaro Black"], "a", "Edward Newgate"],
["\nWho was the first person Luffy fought in the beginning of One Piece?", ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"], "a", "Alvida"] ,
["\nWhat is this highest position within the Marines?",["A. Admiral", "B. Fleet Admiral", "C. Vice Admiral", "D. Grand Admiral"], "b", "Fleet Admiral"],
["\nWhat sound did the Skyipeans hear when the Shandia were sent into the sky via 'the Knock Up Stream'", ["A. Bird", "B. Thunder", "C. Bell", "D. Explosion"], "c", "bell"],
["\nWhat animal is Chopper constantly mistaken for?", ["A. Dog", "B. Squirell", "C. Reindeer", "D. Raccoon"], "d", "raccoon"], 
["\nThere are 10 CP9 agents. How many went undercover at the Galley La shipwright place?", ["A. 4", "B. 6", "C. 5", "D. 3"], "d", "3"],
["\nHow old is Luffy after the time-skip?", ["A. 17", "B. 19", "C. 21", "D. 23"], "b", "19"],
["\nWhat is Katakuri's devil fruit type?", ["A. Paramecia", "B. Logia", "C. Zoan", "D. Smile"], "a", "paramecia"],
["\nWho gave Luffy his scar under his eye?", ["A. Shanks", "B. Black Beard", "C. Demaoro Black", "D. Luffy"], "d", "luffy"]
]

score = 0 # setting the global variable score to 0 

def trivia_stack(my_list):
  # assigning score in function will change the global score and not the local one
  global score 
  question = my_list[0]
  choices = my_list[1]
  answer = my_list[2]
  answer2 = my_list[3]
  print(question)
  for choice in choices:
      print(choice)
  ans = input("\n")
  ans = ans.lower()
  if ans == answer or ans == answer2.lower():
      print("Awesome! Here are 10 points.")
      score = score + 10
  else:
      print(f"\nSorry, that is incorrect. The answer is {answer.title()}. {answer2}")
  print(f"your score is {score}")

#Here, I am looping through my list within a list, within a list, so I can iterate through it while also calling my function inside the loop so, and calling the iterated list as a parameter in my defined function.

for trivia in triviaList:
  trivia_stack(trivia)

#I found out why the code restarts itself. It restarts itself because of the importing of the file (example: import main). 

#^^^Instead of importing the file itself, I have decided to use the global function to add on to the score inside my defined function.

#if-elif statements to print depending on final score.
if score <= 30:
  print(f"\nThis is just terrible {name}! Do you really call yourself a One Piece fan?!")
elif score <= 50:
  print("\nIt could be worse, but I expect more from a One Piece fan.")
elif score <= 70:
  print(f"\nThis is a n above average score. Good job {name}.")
elif score <= 90:
  print("\nThis is pretty amazing. You really do watch One Piece.")
elif score <= 110:
  print(f"\nThis is something else! Good job paying attention in One Piece {name}! you got a perfect score!")
