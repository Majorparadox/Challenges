print("1. \n")
Dictionary = {0 : "Sunday", 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday"}
Day = int(input("What day is it in number form (Saturday = 0, Sunday = 6): "))
Currentday = Dictionary.get(Day)
print(Currentday)

print("2. \n")
Leave = int(input("What day are you leaving(0-6): "))
Length = int(input("How many days will you be gone: "))

Modulus = Length % 7

print(Modulus)

ComebackNum = Leave + Modulus
print(ComebackNum)
if ComebackNum > 6:
    ComebackNum = ComebackNum-7
Comeback = Dictionary.get(ComebackNum)
print(Comeback)

print("3. \n")


print("4. \n")

print("5. \n")

print("6. \n")

print("7. \n")

print("7. \n")

print("8. \n")

print("9. \n")

print("10. \n")

print("11. \n")

print("12. \n")

print("13. \n")

print("14. \n")

print("15. \n")



