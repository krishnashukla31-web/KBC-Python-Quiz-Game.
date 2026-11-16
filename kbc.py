questions = [
    "What is the capital of india?",
    "How many days are there in a leap year?",
    "Who wrote the indian national anthem?",
    "Which planet is known as the red planet?",
    "What is the SI unit of force?"
]
options = [
    ["A.Mumbai", "B. New delhi", "C.kolkata", "D. Chennai"],
    ["A.365", "B.366", "C.364", "D.367"],
    ["A.Bankim chandra", "B.Gandhi", "C.Nehru", "D.Rabindranath tagore"],
    ["A.Venus", "B.Mars", "C.Saturn", "D.Jupiter"],
    ["A.Pascal", "B.Newton", "C.Kilonewton", "D.Joule"],
]
answers = ["B" , "B" , "D" , "B" , "B"]
prizes = [1000, 10000, 100000, 1000000, 10000000]
safe_levels = [10000, 1000000]

winnings = 0
safe_amount = 0

print("WELCOME TO KON BANEGA CROREPATI")
for i in range(len(questions)):
    print(f"question {i + 1} for Rs {prizes[i]}")
    print(questions[i])
    for option in options[i]:
        print(option)
    choice = input("Your answer (A/B/C/D) or Q for quit:").upper()

    if choice =="Q":
        print("You chose to quit")
        break
    elif choice == answers[i]:
        winnings = prizes[i]
        print("Correct!\n")
        if winnings in safe_levels:
            safe_amount = winnings
    else:
        print(f"WRONG!! The correct answer was {answers[i]}")
        print(f"You are taking home rupees{winnings}")
        winnings = safe_amount
        break
else:
    print("\nbbCongratulations!! You are Crorepati!!.")
    print(f"\n You are taking home Rupees {winnings}")
