from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# Create your views here.
# views.py or wherever you're handling requests

def index(request):
    return render(request,"index.html")

def insertData(request):

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        print(name,email,age)
        query=Student(name=name,email=email,age=age)
        query.save()
    return render(request,"index.html")


def show(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request,"show.html",context)

def edit(request):
    return render(request,"edit.html")
def updateData(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        edit = Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.age=age
        edit.save()
        return redirect("/")


    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")


def generate_pdf(request):
    # Fetch data from the database
    data = Student.objects.all()

    # Create a response object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Create a table with the data
    data_table = [['ID', 'Name', 'Age','Email']]  # Adjust field names as per your model
    for item in data:
        data_table.append([item.id, item.name, item.age,item.email])  # Adjust field names as per your model

    # Add style to the table
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    # Create table object and apply style
    data_table = Table(data_table)
    data_table.setStyle(style)

    # Add table to the document
    elements.append(data_table)

    # Build the PDF document
    doc.build(elements)

    return response