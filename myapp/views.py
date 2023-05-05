from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
from myapp.models import Resume



# Create your views here.

def home(request):
    return render(request,'home.html')

def upload(request):
    if request.method == "POST":
        name = str(request.POST["name"])
        email = str(request.POST["email"])
        mobile = str(request.POST["mob"])
        profile = str(request.POST["profile"])
        gender = str(request.POST["gender"])
        state = str(request.POST["state"])
        pin = str(request.POST["pin"])
        resume = request.FILES["resume"]
        upload=Resume(name=name, email=email, mobile=mobile, state=state, profile=profile ,gender=gender, pin=pin,resume=resume )
        upload.save()
        messages.success(request, "Your application has been successfully sent")
    return render(request,'upload.html')



#authentication api's

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
         # check for errorneous input
        if len(username)<5:
            messages.warning(request, " Your user name must not be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('home')

        if User.objects.filter(username = username).first():
            messages.warning(request, "This Username is already taken")
            return redirect('home')

        if User.objects.filter(email = email).first():
            messages.warning(request, "This Email is already taken")
            return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
