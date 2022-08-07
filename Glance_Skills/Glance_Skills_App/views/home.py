from Glance_Skills_App.models.auth import extendeduser
from Glance_Skills_App.models.projects import Project
from django.shortcuts import get_object_or_404, render
from Glance_Skills_App.models import ProjectCategory
from Glance_Skills_App.SerializerCategory import CategorySerial
from django.contrib.auth.models import User
from django.http import JsonResponse

def homepage(request):
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    extra = extendeduser.objects.all()
    context = {
        'categories':categories,
        'projects':projects,
        'extra':extra
    }
    return render(request,'homePage/home.html',context)

def get_category(request):
    cat = ProjectCategory.objects.all()
    get_serilizers = CategorySerial(cat,many=True)
    return JsonResponse(get_serilizers.data,safe=False)

def categorypage(request,pk):
    category = get_object_or_404(ProjectCategory,id=pk)
    project = Project.objects.filter(category=category)
    extra = extendeduser.objects.all()
    context = {
        'category':category,
        'project':project,
        'extra':extra
    }
    return render(request,'homePage/category.html',context)

def aboutuspage(request):
    return render(request, 'homePage/aboutUs.html')