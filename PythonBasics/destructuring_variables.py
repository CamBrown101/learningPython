# t = 5, 11
# x, y = t

# print(x)
# print(y)


# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# print(list(student_attendance.items()))

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")


people = [("Bob", 42, "Mechanic"), ("Cam", 31,
                                    "Developer"), ("Sam", 30, "Boss")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
