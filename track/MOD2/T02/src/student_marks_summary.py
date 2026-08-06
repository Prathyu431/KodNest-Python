student_count=int(input())
total_marks=0
passed_count=0
failed_count=0
for i in range(student_count):
    marks=int(input())
    total_marks=total_marks+marks
    if marks>=40:
        passed_count=passed_count+1
    else:
        failed_count=failed_count+1
print(f"Total marks: {total_marks}")
print(f"Passed students: {passed_count}")
print(f"Failed students: {failed_count}")
if failed_count==0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Improvement Needed")
'''
Output:
3
65
40
80
Total marks: 185
Passed students: 3
Failed students: 0
Batch Result: All Passed
'''