print("Welcome to One Piece Trivia!")
greeting = input("Hello contestant! Ready to play? ")
if greeting == "Yes" or greeting == "yes":
  print("Awesome! Let us get started then.")
else:
  print("\nOk, the program will now shut off.")
  print("\n") 
  quit("Player does not want to play")
#Using the funcition quit(), the program will exit if there is any input besides "Yes" or "yes".

name = input("\nSo, to start off, what is your name? ")
print(f"Nice to meet you {name}!")
print("\nNow, let us get started with our first question")

# I am nesting a list within a list, within a list. This makes it so I will only have to call my defined function one time.
triviaList = [
['\nWho ate the "Chop-Chop" devil fruit?', ["A. Bon Clay", "B. Buggy the Clown", "C. Daz Bones", "D. Clawador"], "b"],
["\nWho was the 3rd person to become member of the Straw Hat Pirates?", ["A. Sanji", "B. Nami", "C. Ussop", "D. Zoro"], "b",],
["\nWhat is White Beard's full name?", ["A. Edward Newgate", "B. Marshal D. Teach", "C. Basil Hawkins", "D. Demoaro Black"], "a"],
["\nWho was the first person Luffy fought in the beginning of One Piece?", ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"], "a"],
["\nWhat is this highest position within the Marines?",["A. Admiral", "B. Fleet Admiral", "C. Vice Admiral", "D. Grand Admiral"], "b"],
["\nWhat sound did the Skyipeans hear when the Shandia were sent into the sky via 'the Knock Up Stream'", ["A. Bird", "B. Thunder", "C. Bell", "D. Explosion"], "c"],
["\nWhat animal is Chopper constantly mistaken for?", ["A. Dog", "B. Squirell", "C. Reindeer", "D. Raccoon"], "d"], ["\nThere are 10 CP9 agents. How many went undercover at the Galley La shipwright place?", ["A. 4", "B. 6", "C. 5", "D. 3"], "d"],
["\nHow old is Luffy after the time-skip?", ["A. 17", "B. 19", "C. 21", "D. 23"], "b"],
["\nWhat is Katakuri's devil fruit type?", ["A. Paramecia", "B. Logia", "C. Zoan", "D. Smile"], "a"],
["\nWho gave Luffy his scar under his eye?", ["A. Shanks", "B. Black Beard", "C. Demaoro Black", "D. Luffy"], "d"]
]

score = 0 #setting the global variable score to 0 

def trivia_stack(my_list):
  global score #assigning to score in function will change the global score and not the local one
  question = my_list[0]
  choices = my_list[1]
  answer = my_list[2]
  print(question)
  for choice in choices:
      print(choice)
  ans = input("\n")
  ans = ans.lower()
  if ans == answer:
      print("Awesome! Here are 10 points.")
      score = score + 10
  else:
      print(f"\nSorry, that is incorrect. The answer is {answer}")
  print(f"your score is {score}")

#Here, I am looping through my list within a list, within a list, so I can iterate through it while also calling my function inside the loop so, and calling the iterated list as a parameter in my defined function.
for trivia in triviaList:
  trivia_stack(trivia)

#I found out why the code restarts itself. It restarts itself because of the importing of the file (example: import main). 

#^^^Instead of importing the file itself, I have decided to use the "global" function to add on to the score inside my defined function.

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
