from django.db import models

# Create your models here.
class Registration(models.Model):
    Gender_choices=[
        ('M','Male')
        ,('F','Female')
    ]
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=25)
    email_id=models.EmailField(max_length=65)
    phone_nu=models.CharField(max_length=10,blank=True,null=True)
    Password=models.CharField(max_length=50,)
    gender=models.CharField(choices=Gender_choices,max_length=1)
    Birthday=models.DateField(max_length=10,null=True,blank=True)
class Information(models.Model):
    user_email=models.EmailField(max_length=65)
    user_password=models.CharField(max_length=50)
    user_phone_nu=models.ForeignKey(Registration,on_delete=models.CASCADE)