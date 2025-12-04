from django.db import models

# Create your models here.

class UserSignup(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=15)
    mobile=models.BigIntegerField()
    
class Mynotes(models.Model):
    submitted_at=models.DateTimeField(auto_now_add=True)
    email=models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    files=models.FileField(upload_to="NotesFolder")
    cate=models.CharField(max_length=100)
    statuschoice=[
        ("Pending","Pending"),
        ("Approve","Approve"),
        ("Reject","Reject")
    ]
    status=models.CharField(choices=statuschoice,max_length=50)
    updated_at=models.DateTimeField(blank=True,null=True)
    

class Contact(models.Model):
    submitted_at=models.DateTimeField(auto_now_add=True)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    msg=models.TextField()