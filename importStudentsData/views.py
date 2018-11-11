import csv , io
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from calculateResults.models import Student , Level , Department

# Create your views here.

@permission_required('admin.can_add_log_entry')
def csv_file_upload(request):
    template="calculateResults/upload_excel_file.html"

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')    

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ',', quotechar="|"):
        _, created = Student.objects.update_or_create(
            student_id=column[0],
            name = column[1],
            level = Level.objects.get(id=column[2]),
            department = Department.objects.get(id=column[3])
        )
    context = {}
    return render(request, template, context)    
