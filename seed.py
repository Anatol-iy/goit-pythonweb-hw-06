import sys
sys.path.insert(0, 'D:/НАВЧАННЯ/9.Fullstack Web Development with Python/goit-pythonweb-hw-06/src')

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from src.models.models import Student, Group, Teacher, Subject, Grade
from faker import Faker
import random
from src.db.connect import engine, Session

# Налаштування Faker
fake = Faker()

# Створення сесії
session = Session()

# Очищення існуючих даних перед заповненням
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Створення груп
groups = []
for i in range(3):
    group_name = fake.word()
    group = Group(name=group_name)
    groups.append(group)
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = []
for i in range(3):
    teacher_name = fake.name()
    teacher = Teacher(name=teacher_name)
    teachers.append(teacher)
session.add_all(teachers)
session.commit()


real_subjects = [
    "Math",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "English",
    "Literature"
]

# Створення предметів
subjects = []
for subject_name in real_subjects:
    teacher = random.choice(teachers)
    subject = Subject(name=subject_name, teacher_id=teacher.id)
    subjects.append(subject)
session.add_all(subjects)
session.commit()

# Створення студентів
students = []
for i in range(30):
    student_name = fake.name()
    group = random.choice(groups)
    student = Student(name=student_name, group_id=group.id)
    students.append(student)
session.add_all(students)
session.commit()

# Створення оцінок
grades = []
for student in students:
    for subject in subjects:
        grade_value = random.randint(1, 12) 
        grade = Grade(grade=grade_value, student_id=student.id, subject_id=subject.id)
        grades.append(grade)
session.add_all(grades)
session.commit()

session.close()

print("Дані успішно додано в базу даних!")
