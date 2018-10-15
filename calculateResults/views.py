from django.shortcuts import render
from django.http import HttpResponse 
from . models import Student , Level

# Create your views here.
def calculateResults(request):
	return render(request , 'calculateResults/calculate_results_form.html')

def displayResults(request):
	students = Student.objects.all()
	context = {
		'students' :students,
	}
	return render(request , 'calculateResults/index.html' , context)

def calculateSubmit(request):
	return HttpResponse("<h1> The form has been submitted! </h1>")	

def search(request):
	error = False
	if 'level' in request.GET:
		q=request.GET['level']
		if not q:
			error = True
		else:
			students = Student.objects.filter(student_level__level_id__icontains=q)
			return render(request , 'calculateResults/calculate_results_form.html' , {'students' : students , 'query': q})
	return render(request, 'calculateResults/calculate_results_form.html' , {'error': error})			
