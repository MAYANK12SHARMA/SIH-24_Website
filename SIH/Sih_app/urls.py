from django.urls import path, include
from Sih_app import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]


urlpatterns = [
    path('', views.index, name='index'),
    path('recognize-speech/', views.recognize_speech, name='recognize_speech'),
]