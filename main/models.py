from django.db import models
from user.models import *


class CoreModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CoreModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(CoreModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FreelancerSkill(CoreModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)  # eg: Beginner, Intermediate, Expert

    def __str__(self):
        return f"{self.user} -- {self.skill}"


class Job(CoreModel):
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'is_client': True})
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(blank=True, null=True)
    skills_required = models.ManyToManyField(Skill, default='Beginner')
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} -- {self.client}"


class Proposal(CoreModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'is_freelancer': True})
    cover_letter = models.TextField()
    proposed_price = models.DecimalField(max_digits=10, decimal_places=2)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='pending')

    def __str__(self):
        return f"{self.job} --> {self.freelancer}"


class Contract(CoreModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='client_contracts')
    end_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job} -- {self.is_completed}"


class Review(CoreModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='given_reviews')
    reviewee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField()

    def __str__(self):
        return f"{self.contract}"


class Resume(CoreModel):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    resume_file = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} -- {self.title}"
