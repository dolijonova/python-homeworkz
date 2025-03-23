import csv


with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    grades_data = list(reader)

# Calculate average grades
subject_totals = {}
subject_counts = {}

for row in grades_data:
    subject = row["Subject"]
    grade = int(row["Grade"])
    if subject in subject_totals:
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    else:
        subject_totals[subject] = grade
        subject_counts[subject] = 1

average_grades = {
    subject: subject_totals[subject] / subject_counts[subject]
    for subject in subject_totals
}


with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    for subject, average in average_grades.items():
        writer.writerow({"Subject": subject, "Average Grade": average})

print("Average grades calculated and saved to average_grades.csv.")