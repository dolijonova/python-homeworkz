# task 1
print("Enter your name")
info=input()
print("Enter the year of your birth")
yb=int(input())
age=2025-yb
print("You are", age, " years old")
# task 2
txt= 'LMaasleitbtui'
car_names=['Lasetti','Malibu']
txt_lower = txt.lower()
found_cars = []
for car in car_names:
    car_lower = car.lower()
    if set(car_lower).issubset(set(txt_lower)):
        found_cars.append(car)
if found_cars:
    print("Found car names:", found_cars)
else:
    print("No car names found in the text.")
# task 3
print("Enter a text/sentence")
sen=input()
length=len(sen)
sen1=sen.swapcase() # type: ignore
print(length,sen1)
# task 4
ispalin=input()
palin=ispalin[::-1]
if palin==ispalin:
    print("word is palindrome")
else:
    print("word is not palindrome")
# task5 
def conscount(word):
    consco=0
    vowelco=0
    vowels={'a','o','e','u','i','y'}
    for char in word:
        if char in vowels:
            vowelco+=1
        elif char.isalpha():
            consco+=1
    return consco, vowelco
wordy=input()
counti=conscount(wordy)
print(counti)
# task 6
print("Enter a string")
string1=input()
print("Enter another string")
string2=input()
if string2 in string1:
    print("The second string is in the first one")
else:
    print("Second string is not in the first one")
# task 7
print(" Enter a sentence ")
sentence=input()
print("Enter a word to replace")
word=input()
print("Enter new word")
replacement=input()
new_sentence=sentence.replace(word,replacement)
print("new sentece", new_sentence)
# task 8
print("Enter a text")
text=input()
firstchar=text[0]
lastchar=text[-1]
print(firstchar," is the first character",lastchar," is the last character")
# task9
print("Enter a text to be reversed")
text2r=input()
reversedtext=text2r[::-1]
print(reversedtext)
# task 10
print("input a sentence")
sentencee=input()
words=sentencee.split()
howmanywords=len(words)
print(howmanywords)
# task 11
print("enter a string to check if there is a number in it")
stringtochecknum=input()
check=any(char.isdigit() for char in stringtochecknum)
if check:
    print("the is a number in a string")
else:
    print( " there is no number in a string")
# task 12
listofwords=input("ENter the list of the words to be in a single string").split()
signinbetween='-'
singlestring=signinbetween.join(listofwords)
print("This is your ingle string",singlestring)
# task15
stringwithgaps=input("ENter a string")
stringwithoutgaps=stringwithgaps.replace(" ","")
# task 14
string11=input()
string22=input()
length1=len(string11)
length2=len(string22)
if length1==length2:
    print("strings are equal")
else:
    print("strings are not equal")
# task 15
acronyms=input()
forwords=acronyms.split()
newwords=""
for word1 in forwords:
    newwords+=word1[0].upper()
print(newwords)
# task 16
stringp=input("Enter a string")
chartoberemoves=input("enter a character to be removed")
nstringp=stringp.replace(chartoberemoves,"")
# task 17
string3=input("enter a string")
vowels={'a','e','u','i','o'}
nstring3=""
for char in string3:
    if char.lower() in vowels:
        nstring3+='*'
    else:
        nstring3+=char
print(nstring3, "your new string")
# task 18
texttocheck=input("ENter a text to check the first and the last word")
firstword=input("enter the frist word")
lastword=input("input the last word")
texttocheck1=texttocheck[len(firstword)]
texttocheck2=texttocheck[-len(lastword)]
if texttocheck1==firstword:
    print("THe first word matches the text")
else:
    print("the first word doesnot match")
if texttocheck2==lastword:
     print("THe last word matches the text")
else:
    print("the last word doesnot match")








