print("1. \n")
n = (1,3,5,7,9,11)
def odd_numbers(n):
    s = sum(n)
    print("The sum of the odd numbers in n is ",s)

odd_numbers(n)

print("2. \n")
E = (2,4,6,8,10,12)
S = sum(E)
print("The sum of all the even numbers is",S)

print("3. \n")
N = (-2,-4,-6,-8,-10,-12)
S = sum(N)
print("The sum of all the negative numbers is",S)

print("4. \n")
count = 0
L = ("words","level", "Bottle", "Water",)

for i in L:
    if len(i) == 5:
        count = count + 1
    else: count = count + 0

print("The total number of words with 5 letter is",count)

print("5. \n")
List = [1,2,4,5,6,7]
x = 0
z = 0
total = 0
print(x)
stop = 0
for i in List:
    if i % 2 == 0 and stop == 0:
        stop = 1
    else:
        total = total + i
print(total)
            
print("6. \n")
List = ("", "Lol", "Ko", "Sam")
Counter = -1

for i in List:
    if List == "Sam":
        break
    else: Counter += 1

print("There are",Counter,"words before Sam")

print("7. \n")
def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better
print(sqrt(25.0))

print("9. \n")
n = int(input("Please enter the number that wants to be triangulated: "))

def triangular(n):
    T = (n*(n+1))/2
    print("The triangular number of",n,"is",T,)

triangular(n)

print("11. \n")
def q11(path):
    import turtle
    canvas = turtle.Screen()
    canvas.setup()
    why = turtle.Turtle()
    why.speed(1)
    for i in range(len(path)):
        why.right(path[i][0])
        why.forward(path[i][1])

path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]


q11(path)

print("12. \n")
def q11(path):
    import turtle
    canvas = turtle.Screen()
    canvas.setup()
    why = turtle.Turtle()
    why.speed(1)
    for i in range(len(path)):
        why.right(path[i][0])
        why.forward(path[i][1])

path = [(270,20),(45,14),(90,14),(135,20),(225,28),(135,20),(135,28),(135,20)]


q11(path)

print("14. \n")
N = -5
y = str(abs(N))
print(len(y))

print("15. \n")
def num_even_digits(n):
    total = 0
    lsit = list(str(abs(n)))
    for i in lsit:
        i = int(i)
        if i % 2 == 0:
            total = total + i
    return total
print(num_even_digits(16428965))

print("16. \n")
List = [1,2,4,5]

def sumofsquares(xs):
    Total = 0
    for i in List:
        square = i**2
        Total += square
    print("The total of the squared numbers is",Total)

sumofsquares(List)

print("17. \n")
Winner = 0

if Winner == 0:
    print("Game Drawn!")
elif Winner == 1:
    print("Human win")
elif Winner == 0:
    print("AI win")
else:
    print("Error")
    break
Replay = int(input("Play again: 1 Stop playing: 0"))
if Replay == 1:
    print("Continue")
elif Replay == 0:
    print("Done")
else:
    print("Error, please enter 1 or 0") #still waiting on the second half of this
