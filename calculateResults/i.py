import csv, sys, os
from django.conf import settings

project_dir ="C:/Users/sarah/Desktop/results/calculateResults"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from CALCULATERESULTS.models import Student

data = csv.reader(open("C:/Users/sarah/Desktop/results/calculateResults/Book1.csv"),delimiter=',')

for row in data:
	if row[0] != 'id':
		student = Student()
		student.id = row[0]
		student.student_id = row[1]
		student.student_name = row[2]
		student.student_level = row[3]
		student.student_department = row[4]
		student.save()
		