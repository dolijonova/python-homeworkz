universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list):
    enrollments=[university[1] for university in list]
    tution_fees=[university[2] for university in list]
    return enrollments,tution_fees

def mean(data):
    mean=round(sum(data)/len(data),2)
    return mean

def median(data):
    sort_data=sorted(data)
    mid=len(data)//2
    if len(sort_data)%2==0:
        median=(sort_data[mid-1]+sort_data[mid])/2
    else:
        median=sort_data[mid]
    return median

enrollments, tution=enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tution)
mean_students = mean(enrollments)
median_students = median(enrollments)
mean_tuition = mean(tution)
median_tuition = median(tution)

print("Total students: ",total_students)
print("Total tuitions: $",total_tuition)
print("Mean students: ",mean_students)
print("Mean tuition: $",mean_tuition)
print("Median students: ",median_students)
print("Median tuitions: $",median_tuition)