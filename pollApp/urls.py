from . import views
from django.urls import path

urlpatterns = [
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('all_polls/',views.all_polls,name='all_polls'),
    path('vote/',views.vote,name='vote'),
    path('result/',views.result,name='result'),
]
