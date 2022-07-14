from . import views
from django.urls import path

urlpatterns = [
    path('',views.signup,name='signup'),
    # path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('all_polls/',views.all_polls,name='all_polls'),
    path('vote/<str:id>',views.vote,name='vote'),
    path('result/<str:id>',views.result,name='result'),
    path('addquestion/',views.addquestion,name='addquestion'),
    path('profilepage/',views.current_user_profile,name='profilepage'),
    path('search_question/',views.search_question,name='search_question')
]