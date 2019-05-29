from django.urls import path, include
from Darwin import views
urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='profile'),
    path('fitnesscheckup/', views.checkup_view, name='fitnesscheckup'),
    path('diagnoseme/', views.diagnose_view, name='diagnoseme'),
    path('visual_checkup/', views.visual_checkup_view, name='visualcheckup'),
    path('mind_checkup/', views.mind_checkup_view, name='mindcheckup'),
    path('heart_checkup/', views.heart_checkup_view, name='heartcheckup'),
    path('facial_checkup/', views.facial_checkup_view, name='facialcheckup'),
    path('result/', views.result_view, name='result'),
]
