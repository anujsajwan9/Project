from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.db.models import fields
from django.forms import ValidationError
from django.forms import ModelForm
from django import forms
from Glance_Skills_App.models import extendeduser

class UserEditForm(ModelForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control loginText','placeholder':"Mobile no",
                'name':"mobileNo",'id':"mobile_no",'min':"10"}))
    profession = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Profession...",
            'name':"profession",'id':"profession"}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Bio......",
        'name':"bio",'id':"bio"}))  

    class Meta:
        model = extendeduser
        fields = ['phone_number','profession','bio','image']
        widgets={
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }


class SignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control loginText','placeholder':"First Name"
                ,'name':"firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control loginText','style':"margin-top: 2rem",
            'placeholder':"Last Name",'name':"lastname",'id':"l_name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control loginText','placeholder':"Username",
                'name':"username",'id':"u_name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control loginText','placeholder':"Email",
                'name':"email",'id':"email_id"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control loginText','placeholder':"Password"
                ,'name':"password",'id':"password"}))
    

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email
        print("user" + user )
        if user is  None:
            raise ValidationError("User Already Exists !!")    



class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control loginText','placeholder':'Enter Your Password','id':'password'}))
    username = forms.EmailField(max_length=20,label='Email Address',required=True,widget=forms.EmailInput(attrs={'class':'form-control loginText','placeholder':'Enter Your Email ID '}))

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        print("1.",email,password,user)
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username,password = password)
            print("2.",user,result)

            if result is not None:
                login(self.request,result)          
            else:
                raise ValidationError("Email or Password Invalid !!!")
        except:
            raise ValidationError("Email or Password Invalid  !!!")


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')