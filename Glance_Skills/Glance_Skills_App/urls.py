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
    path('change-password/',views.ChangePasswordPage.as_view(),name="changePassword"),
    path('feed/',views.FeedPage.as_view(),name='feed'),
    path('feed_delete/<int:pk>/',views.Delete_feed,name='delete_feed'),
    path('like/<int:pk>/',views.LikeView,name='like_post'),
    path('like_profile/<int:pk>/',views.LikeView_profile,name='like_post_profile'),
    path('comment_delete/<int:pk>/',views.Delete_Comment,name='deleteComments'),
    path('createProject/',views.Create_Project,name='createproject'),
    path('myprofile/',views.MyProfile.as_view(),name='myprofile'),
    path('editprofile/',views.EditMyProfile.as_view(),name='editprofile'),
    path('editproject/<int:pk>',views.EditMyProject.as_view(),name='editproject'),
    path('profile_show/<int:pk>/',views.show_profile,name="show_profile"),
    path('project_show/<int:pk>/',views.Show_Project,name="showProject"),
    path('aboutus/',views.aboutuspage,name='aboutus'),
]
