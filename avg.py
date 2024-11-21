'''
    take the input of number n
    and take the number of student name and scores
    and after that find the average mark
    
'''
n = int(input())
student_marks = {}
for _ in range(n):
    data = input().split()
    name = data[0]
    scores = list(map(float, data[1:]))
    student_marks[name] = scores
query_name = input()
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")