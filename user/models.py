from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('erkak', 'erkak'),
    ('ayol', 'ayol')
)
LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Expert', 'Expert')
)


class Profile(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FreelancerSkill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)  # eg: Beginner, Intermediate, Expert

    def __str__(self):
        return f"{self.user} -- {self.skill}"