students_height = input("Enter the height of student heights:").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
count = 0
sum = 0
for total in students_height:
    sum += total
    count += 1;
average = sum/count
con_avg = round(average)
print(f"The average height of students are:{con_avg}")