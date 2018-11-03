print("1-5")
Height = int(input("How  high have you had it with this BS?"))

print("                      ^ Here with your BS")
for i in range(Height):
    print("                      |")

print("\n I have had it up to")
print("Seriously though, one day im gonna do this. Not today though. Sick of turtle >:(")

print("6. \n")
ScoreA = []
ScoreB = []
Rounds = int(input("Please input the number of rounds that took place: "))

for i in range(Rounds):
    WhoWon = input("Please enter A for player A , B for player B or D for a draw: ")
    if WhoWon == "A":
        ScoreA.append(+15)
        ScoreB.append(0)
        print(ScoreA)
        print(ScoreB)
    elif WhoWon == "B":
        ScoreB.append(+15)
        ScoreA.append(0)
        print(ScoreA)
        print(ScoreB)
    elif WhoWon == "D":
        ScoreA.append(0)
        ScoreB.append(0)
        print(ScoreA)
        print(ScoreB)
    elif WhoWon != "A" or "B" or "D":
        print("Please input the correct letter")
