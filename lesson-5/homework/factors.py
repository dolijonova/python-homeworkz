print("Enter an integer: ")
n=int(input())

for i in range(n):
    r=n%(i+1)
    if r==0:
        print(i+1 ,"is the factor of",n)
    else:
        pass
