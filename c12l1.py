#Jacob Sexton 7/8/25

capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Ohio": "Columbus"
}

correct = 0
incorrect = 0

for state in capitals:
    answer = input("What is the capital of " + state + "? ")
    if answer.lower() == capitals[state].lower():
        print("Good Job!")
        correct += 1
    else:
        print("Sorry. The capital of " + state + " is " + capitals[state] + ".")
        incorrect += 1

print("You answered", correct, "correctly and", incorrect, "incorrectly.")
