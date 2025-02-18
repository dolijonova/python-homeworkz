# task1
print("Enter a float number: ")
numberfloat =float(input())
print(round(numberfloat,2))
# task2 
def find_max(num1,num2,num3):
    return max(num3,num1,num2)
def find_min(num1,num2,num3):
    return min(num1,num2,num3)
print("Enter 3 numbers")
num1=int(input())
num2=int(input())
num3=int(input())
largest=find_max(num1,num2, num3)
smallest=find_min(num1,num2,num3)
print(largest, "is the largest number")
print(smallest, "is the smallest number")
# task 3
def km_to_m(km):
    return(km*1000)
def km_to_cm(km):
    return(km*100000)
print("Enter your kilometer")
km=int(input())
km_in_m=km_to_m(km)
km_in_cm=km_to_cm(km)
print(km_in_cm, "cm")
print(km_in_m, "m")
# task 4
print("enter two numbers")