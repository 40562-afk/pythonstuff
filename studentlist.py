students = ["Louis", "Anthony", "Jace", "Antonio", "Travis"]
students_set = set(students)
print(students_set)
grade_set = {90, 80, 70, 4, 89}
students_dict = dict(zip(students_set, grade_set))
print(students_dict)
students_dict = dict.fromkeys(students_set, 71)
print(students_dict)
grade_set = {40, 112, 91, 10, 50}
students_dict = dict(zip(students_set, grade_set))

sum = 0
for grade in students_dict.values():
    sum += grade

print(sum / len(students_dict.values()))
print(dict(sorted(students_dict.items(), key=lambda item: item[1])))

week = ("Sunday", "Monday", "Tuesday", "Wednseday", "Thursday", "Friday", "Saturday")
#lists are changeable and tuples are not

#we use sets when we need unique values, and order does not matter

#we use dictionaries if two values are connected to each other.
