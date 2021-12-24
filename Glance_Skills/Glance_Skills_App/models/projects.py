from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProjectCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/categories/',max_length=150)
    created_date = models.DateTimeField(auto_created=timezone.now())

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=256)
    short_description = models.CharField(max_length=150)
    description = models.CharField(max_length=256)
    likes = models.ManyToManyField(User,related_name='posts')
    image = models.ImageField(upload_to='images/project_images/')
    video = models.FileField(upload_to='video/project_video/')
    external_link = models.URLField(max_length=256)
    created_by = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.project_name



class Projects_Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,related_name='comments',on_delete=models.CASCADE)
    comments = models.TextField()
    created_by = models.DateTimeField(auto_created=timezone.now(),auto_now_add=True)
    updated_by = models.DateTimeField(null=True,blank=True)

