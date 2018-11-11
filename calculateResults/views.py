from django.shortcuts import render
from django.http import HttpResponse 
from . models import Student , Level , Department
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

# Create your views here.
def displayResults(request):
	students = Student.objects.all()
	context = {
		'students' :students,
	}
	return render(request , 'calculateResults/index.html' , context)

def calculateSubmit(request):
	return HttpResponse("<h1> The form has been submitted! </h1>")	

@permission_required('admin.can_add_log_entry')
def search(request):
	levels = Level.objects.all()
	error = False
	if 'level' and 'deptList' in request.GET:
		ql=request.GET['level']
		qd=request.GET['deptList']
		if not ql or not qd :
			error = True 
		else:
			lookups= Q(level__level_name__icontains=ql) & Q(department__department_name__icontains=qd)
			students = Student.objects.filter(lookups)
			return render(request , 'calculateResults/calculate_results_form.html' , {'students' : students , 'queryl': ql , 'levels' : levels})	
	else:		
		return render(request, 'calculateResults/calculate_results_form.html' , {'levels' : levels} , {'error': error} )			
