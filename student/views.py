
from django.db.models import Q
from django.shortcuts import render
from student.models import project
# Create your views here.
def home(request):
    projects = project.objects.all()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)

def home1(request,pk):
    projects = project.objects.get(pk=pk)
    context = {
        "project":projects
    }
    return render(request,'index1.html',context)

def home2(request):
    projects = project.objects.all().values()
    context = {
        "dharani":projects
    }
    return render(request,'index3.html',context)


def home3(request):
    projects = project.objects.values_list('FirstName')
    context = {
        "dharani":projects
    }
    return render(request,'index2.html',context)



def home4(request):
    projects = project.objects.filter(FirstName='Dharani').values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)




def home5(request):
    projects = project.objects.filter(FirstName='Sudhan',id = 12).values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)

def home6(request):
    projects = project.objects.filter(FirstName='Sudhan').values() |  project.objects.filter(FirstName='Dharani').values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)

def home7(request):
    projects = project.objects.filter(Q(FirstName='Elan')| Q(FirstName='Dharani')).values()
    context = {
        "dharani":projects
    }
    return render(request,'index4.html',context)

def home8(request):
    projects = project.objects.filter(FirstName__startswith='M').values()
    context = {
        "dharani":projects
    }
    return render(request,'index5.html',context)

def home9(request):
    projects = project.objects.all().order_by('FirstName').values()
    context = {
        "dharani":projects
    }
    return render(request,'index5.html',context)

def home10(request):
    projects = project.objects.all().order_by('-FirstName').values()
    context = {
        "dharani":projects
    }
    return render(request,'index5.html',context)


def home11(request):
    projects = project.objects.all().order_by('FirstName','-id').values()
    context = {
        "dharani":projects
    }
    return render(request,'index5.html',context)
  
  

def home12(request):
    projects = project.objects.filter(FirstName__contains='rani').values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)
 
def home13(request):
    projects = project.objects.filter(FirstName__endswith='n').values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)



def home14(request):
    projects = project.objects.filter(FirstName__exact='Geetha').values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)

def home15(request):
    projects = project.objects.filter(FirstName__in=['Geetha','Dharani','Janani']).values()
    context = {
        "dharani":projects
    }
    return render(request,'index.html',context)