def convert_cel_to_far(cel):
    far=cel*(9/5)+32
    return far

def convert_far_to_cel(far):
    cel=(far-32)/(9/5)
    return cel

print("Enter a temperature in C: ")
cel1=float(input())
far1=round(convert_cel_to_far(cel1),2)
print(far1)

print("Enter a temperature in F: ")
far2=float(input())
cel2=round(convert_far_to_cel(far2),2)
print(cel2)