from . import views
from django.urls import path


urlpatterns = [
      path('', views.home , name="home" ),
      # path('register/',views.register,name="register"),
      # path('reg_true/',views.reg_true,name="reg_true"),
      # path('dashboard/',views.dashboard,name="dashboard"),
      # path('wallet_view/',views.wallet_view,name="wallet_view"),
      # path('register/<slug:uname>',views.register,name="register"),
      # path('sponsor_val/',views.search,name="sponsor_val"),
      # path('login/',views.login,name="login"),
      # path("logout/", views.logout, name="logout"),
      # path("manage_member/", views.manage_member, name="manage_member"),
      # path("profile/", views.profile_view, name="profile"),
      # path("profile_edit/", views.profile_edit, name="profile_edit"),
      
      
   


      

]