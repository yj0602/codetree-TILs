n = int(input())

class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.total_score = score1 + score2 + score3

students = []

for _ in range(n):
    student_info = input().split()
    name = student_info[0]
    score1, score2, score3 = map(int, student_info[1:])
    student = Student(name, score1, score2, score3)
    students.append(student)

students.sort(key=lambda x: x.total_score)

for student in students:
    print(student.name, student.score1, student.score2, student.score3)