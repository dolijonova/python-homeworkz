def is_prime(n):
    for i in range(n):
        r=n%(i+1)
        if r==0 and (i+1==1 or i+1==n):
            return True
        else:
            return False
        

print("Enter a number to check if its prime or not")
number=int(input())
prime_num=is_prime(number)
print(prime_num)