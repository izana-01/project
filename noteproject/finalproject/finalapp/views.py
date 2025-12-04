from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from finalproject import settings

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    try:
        user=request.session.get("user")
        username=UserSignup.objects.get(email=user)
        if request.method=='POST':
            form=NotesForm(request.POST,request.FILES)
            if form.is_valid():
                x=form.save(commit=False)
                x.status="Pending"
                x.email=username
                x.save()
                print("Notes Subitted!")
                return redirect("/")

            else:
                print(form.errors)
    except:
        print("Error")
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form has been submitted!")
            return redirect('contact')
        else:
            print(form.errors)
    return render(request,'contact.html')

def profile(request):
    uid=request.session.get("uid")
    cid=UserSignup.objects.get(id=uid)
    
    if request.method=='POST':
        form=SignupForm(request.POST,instance=cid)
        if form.is_valid():
            form.save()
            print("Profile Updated!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request,'profile.html',{'cid':cid})

def signin(request):
    if request.method=='POST':
        em=request.POST["email"]
        pa=request.POST["password"]
        
        user=UserSignup.objects.filter(email=em,password=pa)
        uid=UserSignup.objects.get(email=em)
        print(uid.id)
        if user:
            print("Login Successfully!")
            request.session["user"]=em
            request.session["uid"]=uid.id
            return redirect("/")
        else:
            print("Error!Login Faild...")
    return render(request,'signin.html')

otp=0
def signup(request):
    msg=""
    if request.method=='POST':
        email=request.POST["email"]
        user=UserSignup.objects.filter(email=email)
        if user:
            msg="This email address is already exists!"
        else:
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save()
                print("Signup Successfully!")
                
                #Email Sending code
                global otp
                otp=random.randint(11111,99999)
                send_mail(subject="Your OTP",message=f'''Dear User!\n\n
                          Thanks for using our service!\n
                          For account verification your one time password is\n\n
                          {otp}.\n\n
                          Thanks & Regrads\n
                          NotesApp Team\n
                          +91 9825917373 | izana.alvi29@gmail.com''',from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST["email"]])
                print("Email sent successfully!")
                return redirect("otpverify")
            else:
                print(form.errors)
    return render(request,'signup.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('signin')
    
def otpverify(request):
    msg=""
    global otp
    print(otp)
    if request.method=="POST":
        if int(request.POST["otp"])==otp:
            print("Verification Success!")
            return redirect('signin')
        else:
            print("Error!OTP Verification faild...")
            msg="OTP Verification faild...Try again!"
    return render(request,'otpverify.html',{'msg':msg})