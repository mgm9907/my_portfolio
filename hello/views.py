from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
# def test(req):
#     if req.method == 'GET':
#         return redirect(req, 'index.html')

def save(req):
    if req.method == 'GET':
        return render(req, 'index.html')

    else:
        stud = Student(name=req.POST['sname'],
                       email=req.POST['semail'],
                       contact=req.POST['sphone'],
                       subject =req.POST['ssubject'],
                       message=req.POST['smessage'],)
        amsg = "Awesome!! <{}> your data is submited Successfully..."
        stud.save()
        return render(req, 'index.html',{
                                      "student": Student.objects.all(),
                                      "msg": amsg.format(stud.name)})
