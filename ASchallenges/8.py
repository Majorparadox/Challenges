print("1. \n")
print("Python"[1])
#y
print("Strings are sequences of characters."[5])
#g
print(len("wonderful"))
#9
print("p" in "Pineapple")
#True
print("apple" in "Pineapple")
#True
print("pear" not in "Pineapple")
#True
print("apple" > "pineapple")
#False
print("pineapple" < "Peach")
#False

print("2. \n")
prefixes = "JKLMNOPQ"
suffix = "uack"

for i in range(len(prefixes)):
    if prefixes[i] == "O" or prefixes[i] == "Q":
        print(prefixes[i] + suffix)

print("3. \n")
def count_letters(fruit):
    count = 0
    for char in fruit:
        if char == "a":
            count += 1
    print(count)
count_letters("banana")

print("4. \n")
def count_letters(fruit):
    count = 0
    for char in fruit:
        if char == "a":
            count += 1
    print(count)
count_letters("banana")

print("5. \n")
Text = "To make a cake, place five teasponons of sugar. After that place water in and stir thoroughly. Wait 10 minutes for the water to rise."
def remove_punctuation(n):
    Length = len(Text)
    count = 0
    for i in list(Text):
        if i == "e":
            count = count + 1
    Percentage = (count/Length)*100
    print("The total number of E's in a",Length,"words"" is",count,Percentage,"%")

remove_punctuation(Text)

print("6. \n")
layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"

print(layout.format("i", "2i", "3i", "4i", "5i", "6i","7i","8i","9i","10i","11i","12i"))
for i in range(1, 13):
    print(layout.format(i, i*2, i*3, i*4, i*5, i*6,i*7,i*8,i*9,i*10,i*11,i*12))
    
print("7. \n")
String = input("Please enter words to be reversed: ")
def reverse(n):
    Reverse = String[::-1]
    print(Reverse)
reverse(String)

print("8. \n")
String = input("Please enter words to make a palindrome: ")
def mirror(n):
    Reverse = String[::-1]
    print(String+Reverse)
mirror(String)

print("9. \n")
letter = input("Please enter letter to be removed: ")
Words = input("Pleae enter words: ")

def remove_letter(letter, word):
    kansas = list(word)
    for i in range(len(word)):
        if letter != word[i]:
            neword = (word[i])
print(remove_letter(letter,Words))

print("10. \n")
String = input("Please enter words to be reversed: ")
def is_palindrome(n):
    Reverse = String[::-1]
    if String == Reverse:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

is_palindrome(String)


print("11. \n")
Substring = input("Please input the substring: ")
String = input("Please input the string: ")

def count(SS,S):
    print(S.find(SS))
count(Substring,String)

print("12. \n")
def remove(SS,S):
    index = S.find(SS)
    if index < 0:
        return S
    return_str = S[:index] + S[index+len(SS):]
    return return_str

S = input("What is the original string: ")
SS = input("What would you like to remove: ")
print(remove(SS, S))

print("13. \n")
def remove_all(remove, old):
    new_string = old.replace(remove, "")
    return new_string

old = input("What string would you like to remove from?")
remove = input("What would you like to remove from that string?")
print(remove_all(remove, old))
