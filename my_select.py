from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from src.db.connect import engine, Session
from src.models.models import Student, Teacher, Group, Subject, Grade

session = Session()

# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(5).all()
    return result

# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).first()
    return result

# 3. Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    result = session.query(
        Group.name,
        func.avg(Grade.grade).label('average_grade')
    ).join(Student, Student.group_id == Group.id) \
     .join(Grade, Grade.student_id == Student.id) \
     .join(Subject, Subject.id == Grade.subject_id) \
     .filter(Subject.name == subject_name) \
     .group_by(Group.id).all()
    return result


# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    result = session.query(
        func.avg(Grade.grade).label('average_grade')
    ).scalar()
    return result

# 5. Знайти які курси читає певний викладач
def select_5(teacher_name):
    result = session.query(
        Subject.name
    ).join(Teacher).filter(Teacher.name == teacher_name).all()
    return result

# 6. Знайти список студентів у певній групі
def select_6(group_name):
    result = session.query(
        Student.name
    ).join(Group).filter(Group.name == group_name).all()
    return result

# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    result = session.query(
        Student.name,
        Grade.grade
    ).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    return result

# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
# \ для продовження строки
def select_8(teacher_name):
    result = session.query(Teacher.name, func.avg(Grade.grade)) \
        .join(Grade.subject) \
        .join(Subject.teacher) \
        .filter(Teacher.name == teacher_name) \
        .group_by(Teacher.name) \
        .first()
    return result


# 9. Знайти список курсів, які відвідує певний студент
def select_9(student_name):
    result = session.query(
        Subject.name
    ).join(Grade).join(Student).filter(Student.name == student_name).all()
    return result

# 10. Список курсів, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    result = session.query(
        Subject.name
    ).join(Grade).join(Student).join(Teacher).filter(Student.name == student_name, Teacher.name == teacher_name).all()
    return result


session.close()


print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів")
print(select_1())
print("******************************")

print("2. Знайти студента із найвищим середнім балом з певного предмета")
print(select_2("Math"))
print("******************************")

print("3. Знайти середній бал у групах з певного предмета")
print(select_3("Math"))
print("******************************")

print("4. Знайти середній бал на потоці (по всій таблиці оцінок)")
print(select_4())
print("******************************")

print("5. Знайти які курси читає певний викладач")
print(select_5("Emily Greene"))
print("******************************")

print("6. Знайти список студентів у певній групі")
print(select_6("style"))
print("******************************")

print("7. Знайти оцінки студентів у окремій групі з певного предмета")
print(select_7("media", "Math"))
print("******************************")

print("8. Знайти середній бал, який ставить певний викладач зі своїх предметів")
print(select_8("Destiny Atkinson"))
print("---------------------------------")

print("9. Знайти список курсів, які відвідує певний студент")
print(select_9("Christina Warner"))
print("******************************")

print("10. Список курсів, які певному студенту читає певний викладач")
print(select_10("Robin Chavez", "Mario Berg"))
print("******************************")
