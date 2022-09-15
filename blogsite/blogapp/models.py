from django.db import models

# Create your models here.

    
    


class blog(models.Model):
    heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images',null=True)
    desc = models.TextField(max_length=1000000)
    upload_on = models.CharField(max_length=50)
    upload_by = models.CharField(max_length=100)
    datefield = models.DateField(auto_now_add=True)
    

