from re import M


student_scores = input("Enter the marks:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max = 0
for m in student_scores:
     if(max<m):
        max = m

print(f"The higest score in the class is:{max}")