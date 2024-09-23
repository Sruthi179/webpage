# from django.db import models

# Create your models here.


from django.db import models  #This is necessary for creating and managing database tables.
from django.contrib.auth.models import User   #This model handles user authentication and contains fields for basic user information like username and password.

class UserProfile(models.Model):  #In Django, model classes should inherit from models.Model.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)  # New field
    personal_website_url = models.URLField(blank=True)  # New field
    resume = models.FileField(upload_to='resumes/', blank=True)  # New field for resume
    
    def __str__(self):
        return self.user.username
