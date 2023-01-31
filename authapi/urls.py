
from django.urls import path,include
from .views import User_Registration , login

urlpatterns = [
    path('register/', User_Registration.as_view()),
    path('login/', login.as_view())

]
