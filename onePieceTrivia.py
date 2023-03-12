import main

print("Welcome to One Piece Trivia!")
greeting = input("Hello contestant! Ready to play? ")
if greeting == "Yes" or greeting == "yes":
    print("Awesome! Let us get started then.")
else:
    print("\nOk, the program will now shut off.")
    print("\n")
    quit("Player does not want to play")
# Using the function quit(), the program will exit if there is any input besides "Yes" or "yes".

name = input("\nSo, to start off, what is your name? ")
print(f"Nice to meet you {name}!")
print("\nNow, let us get started with our first question")

triviaList = [
['\nWho ate the "Chop-Chop" devil fruit?', ["A. Bon Clay", "B. Buggy the Clown", "C. Daz Bones", "D. Clawador"], "b"],
["\nWho was the 3rd person to become member of the Straw Hat Pirates?", ["A. Sanji", "B. Nami", "C. Ussop", "D. Zoro"], "b", ],
["\nWhat is White Beard's full name?", ["A. Edward Newgate", "B. Marshal D. Teach", "C. Basil Hawkins", "D. Demoaro Black"], "a"],
["\nWho was the first person Luffy fought in the beginning of One Piece?", ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"], "a"],
["\nWhat is this highest position within the Marines?", ["A. Admiral", "B. Fleet Admiral", "C. Vice Admiral", "D. Grand Admiral"], "b"],
["\nWhat sound did the Skyipeans hear when the Shandia were sent into the sky via 'the Knock Up Stream'", ["A. Bird", "B. Thunder", "C. Bell", "D. Explosion"], "c"],
["\nWhat animal is Chopper constantly mistaken for?", ["A. Dog", "B. Squirell", "C. Reindeer", "D. Raccoon"], "d"],
["\nThere are 10 CP9 agents. How many went undercover at the Galley La shipwright place?", ["A. 4", "B. 6", "C. 5", "D. 3"], "d"],
["\nHow old is Luffy after the time-skip?", ["A. 17", "B. 19", "C. 21", "D. 23"], "b"],
["\nWhat is Katakuri's devil fruit type?", ["A. Paramecia", "B. Logia", "C. Zoan", "D. Smile"], "a"],
["\nWho gave Luffy his scar under his eye?", ["A. Shanks", "B. Black Beard", "C. Demaoro Black", "D. Luffy"], "d"]
]

def trivia_stack(my_list):
    #score = 0
    question = my_list[0]
    choices = my_list[1]
    answer = my_list[2]
    print(question)
    for choice in choices:
        print(choice)
    ans = input("\n")
    ans = ans.lower()
    if ans == answer:
        print("\nAwesome! Here are 10 points.")
        main.score += 10
    else:
        print(f"\nSorry, that is incorrect. The answer is {answer}")
    print(f"your score is {main.score}")

# Score is commented out because it needs to be fixed and I will come back to it later.

for trivia in triviaList:
    trivia_stack(trivia)

# I found out why the code restarts itself. It restarts itself because of the importing of the file (example: import main).
# To fix this. I will port in the function exit() to end the program, so it will not restart
print("\nThank you for playing One Piece Trivia!")
exit("Program has concluded")




