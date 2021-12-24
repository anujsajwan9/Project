from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Glance_Skills_App.models.auth import User
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
  


