grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_grades=[]
#for i in range(len(grades)):
#    new_grades.append(sum(grades[i])/len(grades[i]))
new_grades=[sum(grade)/len(grade) for grade in grades]
students = sorted(list(students))
result = {student: new_grades[students.index(student)] for student in students}
#result = {student: new_grades[i] for i, student in enumerate(students)} # Вариант с enumerate

print(result)