from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Glance_Skills_App.models.auth import User
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from Glance_Skills_App.models import Project,Project_Image,extendeduser
from Glance_Skills_App.forms import ProjectImageForm

def Create_Project(request):
    id = request.user.id
    user = get_object_or_404(User,id=id)
    if request.method == 'POST':
        f = ProjectImageForm(request.POST,request.FILES,initial={'user':user})
        files = request.FILES.getlist('image')
        if f.is_valid():
            form = f.save(commit=False)
            print(form)
            form.user = request.user
            form.save()
            for f in files:
                Project_Image.objects.create(project=form,user=request.user,image=f)
            messages.success(request,"Project Created Successfully")
            return redirect('createproject')
    else:
        form = ProjectImageForm(initial={'user':user})
    return render(request, 'project/create_project.html', {'form' : form})

def Show_Project(request,pk):
    project = Project.objects.get(id=pk)
    extra = extendeduser.objects.get(user=project.user)
    project_image = Project_Image.objects.filter(project=project)
    total_project = Project.objects.filter(user=project.user).count()
    context = {
        'project':project,
        'project_image':project_image,
        'extra':extra,
        'total_project':total_project
    }
    return render(request, 'project/fullProjectDetails.html', context=context)

class EditMyProject(View):
    def get(self,request,pk):
        project = Project.objects.get(id=pk)
        context = {
            'project':project
        }
        return render(request,'project/edit_project.html',context)
    
    def post(self,request,pk):
        Project.objects.filter(pk=pk).update(project_name=request.POST['projectName'],description=request.POST['description'],short_description=request.POST['short_desc'],external_link=request.POST['external_link'])
        return HttpResponseRedirect('/myprofile')


  


