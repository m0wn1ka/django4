from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import student
def default(request):
   return HttpResponse("home page")
def subjects(request):
   template = loader.get_template('subjects.html')
   return HttpResponse(template.render())

# Create your views here.
def guide(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
    

# def view2(request):
#   mymembers=student.objects.all().values()
#   template = loader.get_template('studenthtml.html')
#   context={
#      'mymembers' : mymembers,
#   }

#   return HttpResponse(template.render(context,request))


# def view3(request):
#   #mymembers = Member.objects.all().values()
#   template = loader.get_template('html2.html')
#   context ={
#         "data":"Gfg is the best",
#         "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     }
#   return HttpResponse(template.render(context, request))
def  findit(request,id_no):
   mymembers=student.objects.filter(idno=id_no).values()
   # for x in mymembers:
   #    if x.firstname=="NULL":
   #       return HttpResponse("user not found or not registerd")

   template=loader.get_template('studenthtml.html')
   context={
      'mymembers':mymembers,
   }
   return HttpResponse(template.render(context,request))
def exam(request):#exam details
      template = loader.get_template('examdetails.html')
      return HttpResponse(template.render())
def cal(request):#acdemic calender
   template = loader.get_template('calender.html')
   return HttpResponse(template.render())