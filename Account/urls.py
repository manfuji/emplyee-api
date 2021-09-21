from django.urls import path,include
from knox import views as knox_views
from Account.api import RegistrationAPI, LoginAPI, GetUser
from rest_framework import routers
from .views import  ProfileView, Updateprofile,ChangePasswordView,UserViewSet


app_name = 'Account'
router = routers.DefaultRouter()
router.register('updateprofile', Updateprofile,"profile")
router.register(r'users', UserViewSet)

urlpatterns = [
    path("profile/",ProfileView.as_view(),name="profile"),       
    path('auth',include('knox.urls')),
    path('register', RegistrationAPI.as_view(),name = 'register'),
    path('login', LoginAPI.as_view(),name = 'login'),
    path('user', GetUser.as_view(), name='user'),
    path('changepassword', ChangePasswordView.as_view(), name='changepassword'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('logout',knox_views.LogoutView.as_view(), name = 'knox_logout')
]
urlpatterns += router.urls