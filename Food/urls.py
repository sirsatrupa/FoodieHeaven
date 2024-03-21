from django.urls import path
from Food import views

urlpatterns = [
    path('master/', views.master, name='master'),
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='about'),
    path('contactus/', views.contactus, name='contact'),
    path('fooditem/', views.fooditem, name='fooditem'),
    path('<int:item_id>/', views.fooditem, name='fooditemid'),
    path('feedback/', views.feedback, name='feedback'),
    path('signup/', views.signup, name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('seafood/', views.seafood, name='seafood'),
    path('sandwiches/', views.sandwiches, name='sandwiches'),
    path('indianthali/', views.indianthali, name='indianthali'),
     
]
