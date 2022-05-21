n = int(input())
students_records = {}

def avg(values):
    return sum(values)/len(values)


for _ in range(n):
    name, grade_string = input().split(" ")
    grade = float(grade_string)

    if name not in students_records:
        students_records[name] = []
    students_records[name].append(grade)

for name, grades in students_records.items():
    average_grade = avg(grades)
    grades_str = " ".join(str(f"{x:.2f}") for x in grades)
    print(f"{name} -> {grades_str} (avg: {average_grade:.2f})")
