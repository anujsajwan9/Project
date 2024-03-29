from django import forms
from Glance_Skills_App.models import Project,ProjectCategory,Project_Image

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category','project_name','short_description','external_link','image','video','description']

        widgets={
            'category': forms.Select(attrs={'class':'form-control'}),
            'project_name':forms.TextInput(attrs={'class':'form-control loginText'}),
            'short_description': forms.TextInput(attrs={'class':'form-control'}),
            'external_link':forms.URLInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control','multiple':True}),
            'video': forms.FileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }

class ProjectImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta(ProjectForm.Meta):
        fields = ProjectForm.Meta.fields + ['image',]
