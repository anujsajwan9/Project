from django.urls import path
from Glance_Skills_App import views


urlpatterns = [
    path('',views.homepage,name="home"),
    path('categoryPage/<int:pk>/',views.categorypage,name="category"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('register/',views.RegisterView.as_view(),name="signup"),
    path('category/',views.get_category,name='category'),
    path('logout/',views.LogoutView,name="logout"),
    path('reset-password/',views.ResetPasswordPage.as_view(),name="reset_password"),
    path('feed/',views.FeedPage.as_view(),name='feed'),
    path('like/<int:pk>/',views.LikeView,name='like_post'),
    path('like_profile/<int:pk>/',views.LikeView_profile,name='like_post_profile'),
    path('createProject/',views.Create_Project,name='createproject'),
    path('myprofile/',views.MyProfile.as_view(),name='myprofile'),
    path('editprofile/',views.EditMyProfile.as_view(),name='editprofile'),
]
