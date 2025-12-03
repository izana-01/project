from django.shortcuts import render,redirect,get_object_or_404
from finalapp.models import *
import datetime
from django.core.mail import send_mail
from finalproject import settings

# Create your views here.
def admin_home(request):
    if request.method=='POST':
        un=request.POST["username"]
        pa=request.POST["password"]
        
        if un=="admin" and pa=="tops@123":
            print("Login Success!")
            return redirect("admin_dashboard")
        else:
            print("Error!Login Faild...")
    return render(request,'admin_home.html')

def admin_dashboard(request):
    data=UserSignup.objects.all()
    n_data=Mynotes.objects.all()
    n=data.count()
    nd=n_data.count()
    return render(request,'admin_dashboard.html',{'n':n,'nd':nd,'data':data})

def admin_userdata(request):
    data=UserSignup.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    data=Mynotes.objects.all()
    return render(request,'admin_notesdata.html',{'data':data})

def notes_approve(request,id):
    nid=get_object_or_404(Mynotes,id=id)
    nid.status="Approve"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Notes has been approved!")
    
    #Email Sending Code
    sub="Notes has been approved!"
    msg=f"Dear User\n\n Your Notes has been approved by Admin.\n\nThanks for using our services.\n\nThanks & Regards\nNotesApp Team - Admin\n+91 972479949 | sanket.tops@gmail.com"
    from_ID=settings.EMAIL_HOST_USER
    to_ID=[nid.email.email]
    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
    print("Email sent successfully!")
    return redirect('admin_notesdata')

def notes_reject(request,id):
    nid=get_object_or_404(Mynotes,id=id)
    nid.status="Reject"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Notes has been rejected!")
    
    #Email Sending Code
    sub="Notes has been rejecetd!"
    msg=f"Dear User\n\nYour Notes has been rejecetd by Admin.\n\nThanks for using our services.\n\nThanks & Regards\nNotesApp Team - Admin\n+91 972479949 | sanket.tops@gmail.com"
    from_ID=settings.EMAIL_HOST_USER
    to_ID=[nid.email.email]
    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
    print("Email sent successfully!")
    return redirect('admin_notesdata')