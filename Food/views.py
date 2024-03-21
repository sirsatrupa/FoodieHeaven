from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # for sign in
from django.contrib.auth.forms import AuthenticationForm # sign in view
from django.contrib import messages
from .forms import SignupForm
from django.http import HttpResponse

# Create your views here.
def master(request):
    return render(request,"master.html")

def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def fooditem(request):
    item_list = fooditem.objects.all()
    context = {'item_list' : item_list}
    return render(request,"fooditem.html", context)

def seafood(request):
    # sea_item = fooditem.objects.all()
    # context = {
    #     'sea_item': sea_item
    # }
    # return render(request,"seafood.html", context)
    return render(request,"seafood.html")

def sandwiches(request):
    return render(request,"sandwiches.html")

def indianthali(request):
    return render(request,"indianthali.html")

def feedback(request):
    return render(request,"feedback.html")

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            #feed = FeedbackEntry()
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'user': user, })
                # return redirect("/feedback")
    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})

def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have register successfully.')
            return redirect("/home")
    else:
        fm = SignupForm()
    return render(request, "register.html", {'reg_fm':fm})

# Sign out: log out is a built in function
def signout(request):
    logout(request)
    return redirect("/signin")


