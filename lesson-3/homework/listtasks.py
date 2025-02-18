print("1st")
list1=[1,2,4,3,5,4,3,2,5,6]
element=5
occurance=list1.count(element)
print(occurance)
print("2nd")
sumofelements=sum(list1)
print(sumofelements)
print("3rd")
largestel=max(list1)
print(largestel)
print("4th")
smallestel=min(list1)
print(smallestel)
print("5th")
list2=['apple',9,'b',89,'banana',',','book']
elementch=input()
def check(list,element):
    if element in list:
        print("element is in the list")
    else:
        print("element is not in the list")
print(check(list2,elementch))
print("6th")
listf=list1[0]
print(listf)
print("7th")
listl=list1[-1]
print(listl)
print("8th")
list3=list1[:3:]
print(list3)
