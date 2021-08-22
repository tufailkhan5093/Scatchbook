from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class StepsModel(models.Model):
    occasion =  models.CharField(max_length= 225)
    name =  models.CharField(max_length= 225)
    deadline =  models.CharField(max_length= 225)
    objects = models.Manager()

class Occasion(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.CharField(max_length=100)

class Step2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    cover_pic=models.ImageField(upload_to='coverpic',default='coverpic/apple-606761_1920.jpg')
    dead_line=models.DateTimeField(auto_now_add=False)

class Step3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first=RichTextField()
    second=RichTextField()
    third=RichTextField()

class message1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    msg=RichTextField()

class message2(models.Model):
    msg=RichTextField()

class prompt1(models.Model):
    msg=models.CharField(max_length=255)

class prompt2(models.Model):
    msg=models.CharField(max_length=255)

class Sign(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    