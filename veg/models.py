from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recepie(models.Model):
    r_name=models.CharField(max_length=100)
    r_description=models.TextField()
    r_image=models.ImageField(upload_to='recepie_images/')
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.r_name