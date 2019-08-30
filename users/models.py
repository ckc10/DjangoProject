from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    current_employer = models.CharField(max_length=200,default='')
    total_experience = models.CharField(max_length=200,default='')

    def __str__(self):
        return f'{self.user.username} Profile'

#User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
# Create your models here.
