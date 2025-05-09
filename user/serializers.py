from rest_framework import serializers
from .models import Profile, Skill, FreelancerSkill
from django.contrib.auth import get_user_model

User = get_user_model()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class FreelancerSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()  # Nested skill info

    class Meta:
        model = FreelancerSkill
        fields = ['id', 'skill', 'level']


class ProfileSerializer(serializers.ModelSerializer):
    freelancer_skills = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_freelancer', 'is_client', 'phone', 'gender', 'bio',
            'location', 'profile_picture', 'freelancer_skills'
        ]

    def get_freelancer_skills(self, obj):
        if obj.is_freelancer:
            skills = FreelancerSkill.objects.filter(user=obj)
            return FreelancerSkillSerializer(skills, many=True).data
        return []
