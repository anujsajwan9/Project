from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Glance_Skills_App.models.auth import User
from django.views.generic import View
from Glance_Skills_App.models import Project
from Glance_Skills_App.forms import ProjectForm

def Create_Project(request):
    id = request.user.id
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        f = ProjectForm(request.POST, request.FILES,initial={'user':user})
        if f.is_valid():
            form = f.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request,"Project Created Successfully")
            return redirect('createproject')
    else:
        form = ProjectForm(initial={'user':user})
    return render(request, 'project/create_project.html', {'form' : form})

def Show_Project(request,pk):
    project = Project.objects.get(id=pk)
    return render(request, 'project/fullProjectDetails.html', {'project' : project})

class EditMyProject(View):
    def get(self,request,pk):
        project = Project.objects.get(id=pk)
        context = {
            'project':project
        }
        return render(request,'project/edit_project.html',context)
    
    def post(self,request):                
        return render(request,'project/edit_project.html')    


  


