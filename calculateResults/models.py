from django.db import models

# Create your models here.
class Level(models.Model):
	level_id = models.IntegerField()
	level_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.level_name

class Department(models.Model):
	department_id = models.IntegerField()
	department_name = models.CharField(max_length = 100)	

	def __str__(self):
		return self.department_name
	
class Student(models.Model):
	student_id = models.IntegerField()
	student_name = models.CharField(max_length=100)
	student_level = models.ForeignKey(Level , on_delete = models.CASCADE)
	student_department = models.ForeignKey(Department , on_delete = models.CASCADE)

	def __str__(self):
		return self.student_name
	
class Subject(models.Model):
	subject_id = models.IntegerField()
	subject_code = models.CharField(max_length=100)
	subject_name = models.CharField(max_length=100)
	level_name = models.ForeignKey(Level , on_delete = models.CASCADE)	
	department_name = models.ForeignKey(Department , on_delete = models.CASCADE)

class Grade(models.Model):
	student_id = models.ForeignKey(Student , on_delete = models.CASCADE)
	student_name = models.CharField(max_length=100)	
	subject_id = models.ForeignKey(Subject , on_delete = models.CASCADE)
	grade = models.IntegerField()
