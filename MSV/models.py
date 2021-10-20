from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name, self.last_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    mobile_no = models.PositiveSmallIntegerField(null=True)
    image = models.ImageField(null=True, default='download_1.png')
    bio = models.TextField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()


class Templates(models.Model):
    CHOICE = (
        ('Random', 'Random'), ('Anime', 'Anime'),
        ('Cartoon', 'Cartoon'), ('Celebrity', 'Celebrity'), ('Web series', 'Web series'),
    )
    category = models.CharField(max_length=12, choices=CHOICE)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.category


class Video(models.Model):
    CHOICE = (
        ('Celebrity', 'Celebrity'),
        ('Vira', 'Viral'), ('Movies', 'Movies'), ('Web series', 'Web series'),
        ('Funny', 'Funny'), ('Abusive', 'Abusive'),
    )
    category = models.CharField(max_length=12, choices=CHOICE)
    video = models.FileField(null=True)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
