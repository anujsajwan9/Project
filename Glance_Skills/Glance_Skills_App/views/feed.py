# from Glance_Skills.Glance_Skills_App.models.projects import Project_CommentsReply
from Glance_Skills_App.models import projects
from Glance_Skills_App.models.projects import ProjectCategory, Projects_Comment
from abc import abstractmethod
import django
from django.db.models.deletion import PROTECT
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from Glance_Skills_App.forms.authform import UserEditForm,UserForm
from Glance_Skills_App.models import Project
from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User

from Glance_Skills_App.models import Project,extendeduser

class FeedPage(View):

    def get(self,request):
        user = User.objects.get(username=request.user)
        extradetail_user = extendeduser.objects.get(user=user) 
        project = Project.objects.all().exclude(user=user)
        categories =  ProjectCategory.objects.all()
        liked_project = Project.objects.filter(likes=request.user)
        # reply =  Project_CommentsReply.objects.filter(comment = )
        
        context = {
            'projects':project,
            'user':user,
            'extra':extradetail_user,
            'liked_project':liked_project,
            'categories':categories
            
        }
        return render(request,'feed/feed_main.html',context)

    def post(self,request):
        get_project = get_object_or_404(Project,id=request.POST.get('project_id'))
        comment_add = Projects_Comment.objects.create(user=request.user,project=get_project,comments=request.POST.get('user_comment'))
        a = comment_add.save()
        return HttpResponseRedirect(reverse('feed'))


        # LIKE FUNCTION


def LikeViewFunction(request,pk):
    project = get_object_or_404(Project,id=request.POST.get('project_id'))
    liked = False
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        liked= False
    else:
        project.likes.add(request.user)
        liked = True 
        # END FUNCTION
 
def LikeView(request,pk):
    likin = LikeViewFunction(request,pk)
    return HttpResponseRedirect(reverse('feed'))

def LikeView_profile(request,pk):
    likin = LikeViewFunction(request,pk)
    return HttpResponseRedirect(reverse('myprofile'))


class MyProfile(View):
    def get(self,request):
        extradetails = extendeduser.objects.get(user=request.user)
        projects = Project.objects.filter(user=request.user)
        liked_project = Project.objects.filter(likes=request.user)
        for project in projects:
            print(project.user.extendeduser.image.url)
        context = {
            'extradetails':extradetails,
            'projects':projects,
            'project_counts':projects.count(),
            'liked_project':liked_project,
        }
        return render(request,'feed/myprofile.html',context)

    def post(self,request):
        get_project = get_object_or_404(Project,id=request.POST.get('project_id'))
        comment_add = Projects_Comment.objects.create(user=request.user,project=get_project,comments=request.POST.get('user_comment'))
        a = comment_add.save()
        return HttpResponseRedirect(reverse('myprofile'))


class EditMyProfile(View):
    def get(self,request):
        user = User.objects.get(username=request.user)
        extradetails = extendeduser.objects.get(user=request.user)
        form = UserForm(instance=user)
        forms = UserEditForm(instance=extradetails)
        context = {
            'form':form,
            'forms':forms,
            'extra':extradetails
        }
        return render(request,'feed/feed_editmyprofile.html',context)
    
    def post(self,request):        
        profile_model = get_object_or_404(extendeduser, user=request.user)
        user_model = User.objects.get(username = request.user)
        form = UserForm(request.POST or None,request.FILES or None,instance=user_model)
        forms = UserEditForm(request.POST, request.FILES,instance=profile_model)
        if form.is_valid():
            f = form.save(commit=False)
            forms.save()
            return redirect('editprofile')
        context = {'form': form,'forms':forms, 'extra':profile_model}          
        return render(request,'feed/feed_editmyprofile.html',context)    

