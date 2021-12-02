
from django.contrib.auth.models import User
from django.db import models
 
class UserProfile(models.Model):
    '''
    Our UserProfile model extends the built-in Django User Model
    This is specific to the user! i.e. the individual that signs up
    '''
    class Meta:
        verbose_name_plural = 'User Profiles'
        ordering = ["id"]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default = False)
 