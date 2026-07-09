students = []
while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    marks = float(input("Enter marks for " + name + ": "))
    students.append({"name": name, "marks": marks})
print("\nAll students entered!")
total = 0
highest = students[0]["marks"]
lowest = students[0]["marks"]
highest_student = students[0]["name"]
lowest_student = students[0]["name"]
for student in students:
    total += student["marks"]
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]
    if student["marks"] < lowest:
        lowest = student["marks"]
        lowest_student = student["name"]
average = total / len(students)
print("\n--- Results ---")
print("Average marks: " + str(round(average,2)))
print("Highest: " + highest_student + " with " + str(highest) + " marks")
print("Lowest: " + lowest_student + " with " + str(lowest) + " marks")
print("There are " + str(len(students)) + " students in total.")
