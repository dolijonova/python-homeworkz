# task4
def remainder(number,divisor):
    result=int(number/divisor)
    remainder=number-(result*divisor)
    return remainder
print("Input two numbers")
num=int(input())
divisor=int(input())
result=int(num/divisor)
rem=remainder(num,divisor)
print(result," is the result",rem," is the remainder")
# task5 
def converter(celcius):
    f=(9/5*celcius)+32
    return f
print("Enter you celcius value")
cel=int(input())
feh=converter(cel)
print(feh, " is the the Fahrenheit value")
# task6
def lastdigit(num):
    h=int(num/10)
    lastd=num-(h*10)
    return lastd
print("Enter a number")
num2=int(input())
lastd=lastdigit(num2)
print( lastd, "is the last digit of the number")
# task7
def evenorodd(num):
    if num%2==0:
        return True
    else:
        return False
print("Enter a number to check if its even")
num3=int(input())
numberis=evenorodd(num3)
if numberis:
    print("Number is even")
else:
    print("Number is odd")