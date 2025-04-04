from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.models.base import Base


# Таблиця студентів
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

# Таблиця груп
class Group(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    students = relationship('Student', back_populates='group')

# Таблиця викладачів
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    subjects = relationship('Subject', back_populates='teacher')

# Таблиця предметів
class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=False)
    
    teacher = relationship('Teacher', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')

# Таблиця оцінок
class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    grade = Column(Float, nullable=False)
    date_received = Column(DateTime, default=datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    
    student = relationship('Student', back_populates='grades')
    subject = relationship('Subject', back_populates='grades')
