from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank_profile_picture.avif')
    location = models.CharField(max_length=100, blank=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)
    
    

    def __str__(self):
        return self.user.username