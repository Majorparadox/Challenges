print("1. \n")
def turn_clockwise(n):
    if n == "n" or n == "N":
        print("East")
    elif n == "e" or n == "E":
        print("South")
    elif n == "s" or n == "S":
        print("West")
    elif n == "w" or n == "W":
        print("North")
Input = input("Please enter the compass point")
n = Input
turn_clockwise(n)

print("2. \n")
def day_name(n):
    if n == 0:
        print("Sunday")
    elif n == 1:
        print("Monday")
    elif n == 2:
        print("Tuesday")
    elif n == 3:
        print("Wednesday")
    elif n == 4:
        print("Thursday")
    elif n == 5:
        print("Friday")
    elif n == 6:
        print("Saturday")
    elif n >= 7:
        print("None")
input = int(input("Please enter a number from 0 to 6: "))
n = input
day_name(n)

print("3. \n")
def day_name(n):
    if n == "Sunday":
        print("0")
    elif n == "Monday":
        print("1")
    elif n == "Tuesday":
        print("2")
    elif n == "Wednesday":
        print("3")
    elif n == "Thursday":
        print("4")
    elif n == "Friday":
        print("5")
    elif n == "Saturday":
        print("6")
    else:
        print("None")
inpu = input("Please enter the day: ")
n = inpu
day_name(n)

print("4. \n")
day = int(input("Please enter the day where Monday is 1 and Sunday is 7. "))
d = day
def day_name(n):
    if n == 0:
        print("Sunday")
    elif n == 1:
        print("Monday")
    elif n == 2:
        print("Tuesday")
    elif n == 3:
        print("Wednesday")
    elif n == 4:
        print("Thursday")
    elif n == 5:
        print("Friday")
    elif n == 6:
        print("Saturday")
    elif n >= 7:
        n%7
        if n%7 == 0:
            print("Sunday")
        elif n%7 == 1:
            print("Monday")
        elif n%7 == 2:
            print("Tuesday")
        elif n%7 == 3:
            print("Wednesday")
        elif n%7 == 4:
            print("Thursday")
        elif n%7 == 5:
            print("Friday")
        elif n%7 == 6:
            print("Saturday")
day_name(d)

print("5. \n")
def day_name(n):
    if n == 0:
        print("Sunday")
    elif n == -6:
        print("Monday")
    elif n == -5:
        print("Tuesday")
    elif n == -4:
        print("Wednesday")
    elif n == -3:
        print("Thursday")
    elif n == -2:
        print("Friday")
    elif n == -1:
        print("Saturday")
    elif n >= 7:
        print("None")

input = int(input("Please enter the - number when the day is Sunday "))
n = input

day_name(n)

print("6. \n")
def days_in_months(n):
    if n == "January":
        print("31 days")
    elif n == "February":
        print("28 days")
    elif n == "March":
        print("31 days")
    elif n == "April":
        print("30 days")
    elif n == "May":
        print("31 days")
    elif n == "June":
        print("30 days")
    elif n == "July":
        print("31 days")
    elif n == "August":
        print("31 days")
    elif n == "September":
        print("30 days")
    elif n == "October":
        print("31 days")
    elif n == "November":
        print("30 days")
    elif n == "December":
        print("31 days")
    else:
        print("None")
n = input("Please enter the month: ")
days_in_months(n)

print("7. \n")
def to_secs(h,m,s):
    h *= 3600
    m *= 60
    print(h+m+s)

Hours = int(input("Please input the hours: "))
h = Hours
Minutes = int(input("Please input the minutes: "))
m = Minutes
Seconds = int(input("Please input the seconds: "))
s = Seconds

to_secs(h,m,s)

print("8. \n")
def to_secs(h,m,s):
    h *= 3600
    m *= 60
    print(h+m+s)
Hours = float(input("Please input the hours: "))
h = int(Hours)
Minutes = float(input("Please input the minutes: "))
m = int(Minutes)
Seconds = float(input("Please input the seconds: "))
s = int(Seconds)
to_secs(h,m,s)

print("9. \n")
input = int(input("Please enter the total number of seconds: "))

def to_secs(n):
    h = input/3600
    print("The total hours in", input, "seconds is",h, "hours" )
    m = ((input/3600)/60)
    print("The total minutes left in", input/3600, "is",m, "minutes" )
    s = input - ((input/3600)/60)
    print("The total seconds left in", ((input/3600)/60), "is",s, "seconds" )

to_secs(input)

print("10. \n")
test(3 % 4 == 0)
#Remainder should be 2
test(3 % 4 == 3)
#Remainder should be 2
test(3 / 4 == 0)
#0.75
test(3 // 4 == 0)
#Not possible
test(4-2+2 == 0)
#4

print("11. \n")
a = int(input("Please enter value of a: "))
b = int(input("Please enter value of b: "))

if a > b :
    print(1)
elif a == b:
    print(0)
elif a < b:
    print(-1)

print("12. \n")
L1 = int(input("Please enter the length of one side of the right-angled triangle: "))
L2 = int(input("Please enter the length of the other side of the right-angled triangle: "))

def hypotenus(a,b):
    L3 = ((L1**2) + (L2**2))**0.5
    print("The hypetenus of", L1, "And", L2, "is",L3,)

hypotenus(L1,L2)

print("13. \n")
x1 = int(input(" Please enter the x coordinate of the first point: "))
y1 = int(input(" Please enter the y coordinate of the first point: "))
x2 = int(input(" Please enter the x coordinate of the second point: "))
y2 = int(input(" Please enter the y coordinate of the second point: "))


def slope(x1, y1, x2, y2):
    Gradient = (y1-y2)/(x1-x2)
    print("The gradient of the line is",Gradient,)

slope(x1,y1,x2,y2)

def intercept(x1, y1, x2, y2):
    Gradient = (y1-y2)/(x1-x2)
    y = Gradient*-x1 + y1
    print("The y-intercept is",y,)

intercept(x1,y1,x2,y2)

print("14. \n")
n = int(input("Please enter the number: "))

def is_even(n):
    if n/2 == int(n/2):
        print("True")
    else: print("False")

is_even(n)

print("15. \n")
n = int(input("Please enter the number: "))

def is_even(n):
    if n/2 == int(n/2):
        print("True")
    else: print("False")

def is_odd(n):
    if n/2 == int(n/2):
        print("The number is even")
    else: print("The number is odd")

is_even(n)
is_odd(n)

print("16. \n")
Number = int(input("Please enter the number: "))
Factor = int(input("Please enter the factor: "))


def is_Factor(f,n):
    if Number/Factor == int(Number/Factor):
        print("The factor of ",Number,"is", Factor)
    else: print("Not a factor")

is_Factor(Number,Factor)

print("17. \n")
n = int(input("Please enter the number: "))
m = int(input("Please enter the multiple: "))


def is_multiple(m,n):
    if n/m == int(n/m):
        print(m, "is a multiple of",n)
    else: print("Not a multiple")

is_multiple(m,n)

print("18. \n")
F = float(input("Please enter the temperature in Fahrenheit: "))

def f2c(t):
    C = (F-32)/(9/5)
    print("The temperature of",F,"Fahrenheit in Celcius is",C)

f2c(F)

print("19. \n")
C = float(input("Please enter the temperature in Celcius: "))

def c2f(t):
    F = (C*(9/5)) +32
    print("The temperature of",C,"Celcius in Fahrenheit is",F)

c2f(C)
