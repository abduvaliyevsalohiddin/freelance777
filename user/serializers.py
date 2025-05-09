from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    freelancer_skills = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_freelancer', 'is_client', 'phone', 'gender', 'bio',
            'location', 'profile_picture', 'freelancer_skills'
        ]

    # def get_freelancer_skills(self, obj):
    #     if obj.is_freelancer:
    #         skills = FreelancerSkill.objects.filter(user=obj)
    #         return FreelancerSkillSerializer(skills, many=True).data
    #     return []
