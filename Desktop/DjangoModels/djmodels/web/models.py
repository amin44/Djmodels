from django.db import models
from django.utils.encoding import smart_text
from django.core.exceptions import ValidationError
# Create your models here.

GENDER_CHOICES=(('male','Male'),('female','Female'))

def validate_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("not correct format")

class Post(models.Model):
    id=models.BigAutoField(primary_key=True)
    active=models.BooleanField(default=True)
    title=models.CharField(max_length=100,unique=True)
    content=models.TextField(null=True,blank=True,verbose_name="write about title")
    Gender=models.CharField(max_length=100,default="Male",choices=GENDER_CHOICES)
    publish_date=models.DateField(auto_now=False,auto_now_add=False,verbose_name="Publish Date")
    email=models.CharField(max_length=100,null=True,blank=True,verbose_name="Your Email",validators=[validate_email])
    # better work is use models.EmailField
    def __str__(self):
        return smart_text(self.title)